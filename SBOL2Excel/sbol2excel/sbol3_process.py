"""
Presented here are a grouping of SBOL3 preocesing functions.

These functions assist information from the SBOL3 file.
"""
import sbol3
import sbol2excel.ontology_methods as om
import sbol2excel.sheet_methods as sm
import sbol2excel.helper_functions as hf
import sbol2excel.column_methods as cm
import pandas as pd


def sbol3_converter(sbol_doc_path, output_path):
    """Set up the dataframe's output chart.

    This function handles setting up which columns
    of the dataframe will be output into Excel.
    """
    onto_version = 'ontologies_v001.xlsx'
    output_template = 'Output_Template_v001.xlsx'
    col_list = ['Identity',
                'Part Name',
                'Role',
                'Design Notes',
                'Altered Sequence',
                'Part Description',
                'Data Source Prefix',
                'Data Source',
                'Source Organism',
                'Target Organism',
                'Circular',
                'length (bp)',
                'Sequence',
                'Data Source',
                'Composite']
    drop_list = ['Persistentidentity',
                 'Displayid',
                 'Version',
                 'Attachment',
                 'Types',
                 'OBI_0001617']

    role_dict = om.role_ontology(onto_version)
    org_dict = om.organism_ontology(onto_version)

    # read in sbol data
    df = sbol3_to_df(sbol_doc_path, role_dict, org_dict)

    # reorder columns based on list above
    df = hf.reorder_col(df, col_list)

    # drop columns in the drop list
    drop_list_intersect = [elem for elem in drop_list if elem in df.columns]
    df = df.drop(columns=drop_list_intersect)

    # output to excel
    sm.df_to_excel(df, output_path, output_template)
    return


def sbol3_to_df(sbol_doc_path, role_dict, org_dict):
    """Read in an sbol3 file and returns a dataframe.

    The dataframe will be output with uri/persistent identity of
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
    # create document object
    doc = sbol3.Document()
    doc.read(sbol_doc_path)

    # create a dictionary to hold all the component defintions' information
    cd_dict = {}

    # iterate through the component definitions
    for c in doc.objects:
        # create a dictionary that has a key for the
        # component definition's identity,
        # and a value for all of its features
        comp_features = {}
        cd_uri = c.identity
        # iterate through the properties of the component defintions
        # and set them equal to prop_val variable
        for prop in c.properties:
            # ********** AJs Test **********
            try:
                # log issue for this section in SBOL3
                prop_val = c[prop]
            except ValueError:
                print(type(c))
                prop_val = []
            # ********** AJs Test **********
            # extract attribute property type
            if prop_val == []:
                prop_val = ''
            print(prop_val)
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
