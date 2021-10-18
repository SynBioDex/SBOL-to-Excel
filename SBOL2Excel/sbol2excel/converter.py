"""This module features the dataframe's prearrangement."""

import sbol2excel.sheet_methods as sm
import sbol2excel.ontology_methods as om
import sbol2excel.helper_functions as hf


def converter(sbol_doc_path, output_path):
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
    df = sm.sbol_to_df(sbol_doc_path, role_dict, org_dict)

    # reorder columns based on list above
    df = hf.reorder_col(df, col_list)

    # drop columns in the drop list
    drop_list_intersect = [elem for elem in drop_list if elem in df.columns]
    df = df.drop(columns=drop_list_intersect)

    # output to excel
    sm.df_to_excel(df, output_path, output_template)
    return
