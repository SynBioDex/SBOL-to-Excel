"""This module features the formatting of the dataframe.

The dataframe will be prepared to be output in Excel format.

"""

import os
import pandas as pd
from openpyxl import load_workbook
from openpyxl.worksheet.table import Table, TableStyleInfo
from openpyxl.utils.dataframe import dataframe_to_rows
from rdflib import Graph
import sbol2excel.ontology_methods as om
import sbol2excel.column_methods as cm
import sbol2excel.helper_functions as hf
import logging


def sbol_to_df(sbol_doc_path, role_dict, org_dict):
    """Utilize RDFLib to collect document contents."""
    g = Graph()
    g.parse(sbol_doc_path)
    subj = {}
    for index, (subject, predicate, _object) in enumerate(g):
        # collect subject, predicate, and object triples
        subject = str(subject)
        # subject = om.prop_convert(subject)
        predicate = str(predicate)
        predicate = str(om.prop_convert(str(predicate)))
        _object = str(_object)
        # process the object to make it more human readable
        _object = cm.col_methods(predicate, _object, role_dict,
                                    org_dict).prop_val
        # create dataframe the prepares the triples to be output to excel
        if subject in subj:
            if predicate in subj[subject]:
                subj[subject][predicate] = subj[subject][predicate] + _object + " "
            else:
                subj[subject][predicate] = _object
        else:
            subj[subject] = {predicate: _object}
    df = pd.DataFrame.from_dict(subj, orient='index')
    # df = om.prop_convert(df)
    return df


def df_to_excel(df, output_path, output_template):
    """Output a df into an excel template.

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
    output_template_path = os.path.join(SBOL2Excel_path, 'sbol2excel',
                                        'Output_Templates', output_template)
    # ********** TEMPORARY COMMENT OUT **********
    if not os.path.isfile(output_template_path):
        raise ValueError
    # ********** TEMPORARY COMMENT OUT **********
    wb = load_workbook(output_template_path)
    ws = wb.active
    df_row_obj = dataframe_to_rows(df, index=False, header=True)

    # empty row added to maintain space between previous full row and
    # the table of parts inserted
    ws.append([])

    # add df information
    for row in df_row_obj:
        ws.append(row)

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
