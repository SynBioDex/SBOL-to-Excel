import os
import sbol2
import pandas as pd
from openpyxl import load_workbook
from openpyxl.worksheet.table import Table, TableStyleInfo
from openpyxl.utils.dataframe import dataframe_to_rows
import utils.ontology_methods as om
import utils.column_methods as cm
import utils.helper_functions as hf
import logging


def sbol_to_df(sbol_doc_path, role_dict, org_dict):
    """Reads in an sbol file and returns a df with uri/persistent identity of
    each component defintion as index and each property being a column


    Args:
        sbol_doc_path (string): full file path to the sbol document to read in
        role_dict (dictionary): dictionary to convert role uris to human
                        readable format.
                        E.g. {'http://identifiers.org/so/SO:0000316': 'CDS'}
        org_dict (dictionary): dictionary to convert organism ncbi txid
                        uris to human readable format.
                        E.g. {'21': 'Phenylobacterium immobile'}

    Raises:
        ValueError: if the sbol_doc_path does not point to a file

    Returns:
        pandas dataframe: a dataframe with uri/peristent identity as
                    index and properties of the sbol component definitions
                    as columns. If a property doesn't exist for a component
                    definition then pd.nan is used to fill the gap
    """

    doc = sbol2.Document()

    if os.path.isfile(sbol_doc_path):
        doc.read(sbol_doc_path)
    else:
        raise ValueError

    # create a dictionary to hold all the component defintions' information
    cd_dict = {}

    # iterate through the component definitions
    for cd in doc.componentDefinitions:
        # create a dictionary that has a key for the
        # component definition's identity,
        # and a value for all of its features
        comp_features = {}
        cd_uri = cd.identity

        # iterate through the properties of the component defintions
        # and set them equal to prop_val variable
        for prop in cd.properties:
            try:
                prop_val = cd.properties[prop][0]
            except IndexError:
                prop_val = cd.properties[prop]
                # extract attribute property type
            if prop_val == []:
                prop_val = ''
            prop = om.prop_convert(prop)
            prop_val = cm.col_methods(prop, prop_val, doc, role_dict,
                                      org_dict).prop_val
            comp_features[prop] = str(prop_val)

        # append each comp_features dictionary as a
        # value into the component definitions
        # dictionary with the persistentIdentity/uri serving as the key
        cd_dict[cd_uri] = comp_features

    doc_df = pd.DataFrame.from_dict(cd_dict, orient="index")

    return doc_df


def df_to_excel(df, output_path, output_template):
    """Outputs a df into an excel template

    Args:
        df (pandas dataframe): The dataframe to put into the excel
                spreadsheet
        output_path (file path): Path to where the new excel file should
                be output
        output_template (string): the name of the output template to use

    Raises:
        TypeError: if df is not a pandas dataframe
        ValueError: if the output_template is not a valid name
    """
    # input type checking
    if type(df) is not pd.core.frame.DataFrame:
        raise TypeError

    # first row to put data into (one below last filled row)
    start_row = 19
    # first cell to put data into, by default the column data is put into is A
    up_l_tbl_cell = f"A{start_row}"

    df_num_rows = len(df)
    df_num_cols = len(df.columns)
    bt_r_tbl_cell = f"{hf.col_to_num(df_num_cols)}{df_num_rows+start_row}"

    # load workbook
    file_dir = os.path.dirname(__file__)
    SBOL2Excel_path = os.path.split(file_dir)[0]
    output_template_path = os.path.join(SBOL2Excel_path, 'utils',
                                        'Output_Templates', output_template)
    if not os.path.isfile(output_template_path):
        raise ValueError
    wb = load_workbook(output_template_path)
    ws = wb.active
    df_row_obj = dataframe_to_rows(df, index=False, header=True)

    # empty row added to maintain space between previous full row and
    # the table of parts inserted
    ws.append([])

    # add df information
    for row in df_row_obj:
        ws.append(row)

    # create table in information area
    tab = Table(displayName="Table1", ref=f"{up_l_tbl_cell}:{bt_r_tbl_cell}")

    # style the table
    style = TableStyleInfo(name="TableStyleLight4",
                           showFirstColumn=False,
                           showLastColumn=False,
                           showRowStripes=True,
                           showColumnStripes=False)
    tab.tableStyleInfo = style
    ws.add_table(tab)

    # Save
    wb.save(output_path)
    logging.warning(f'Your converted file has been output at {output_path}')
