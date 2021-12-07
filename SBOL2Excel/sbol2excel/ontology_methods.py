"""This module handles the fetching of ontology terms."""
# from typing import Counter
import sbol2excel.helper_functions as hf
import pandas as pd
import os


def role_ontology(onto_version):
    """Read in a role ontology sheet from the sbol2excel/Ontology sheets folder.

    Reads in based on the onto_version supplied

    Args:
        onto_version (string): the name of the file in the Ontology Sheets
                            folder to read in

    Raises:
        TypeError: The onto_version supplied is not a string
        ValueError: The onto_version supplied does not point to a file in the
                    Ontology Sheets folder

    Returns:
        dictionary: Dictionary of the organisms of the form
            {'role_uri': 'Role Name'}, e.g.
            {'http://identifiers.org/so/SO:0000167': 'promoter',
            'http://identifiers.org/so/SO:0000139': 'ribosome_entry_site}
    """
    if type(onto_version) is not str:
        raise TypeError

    file_dir = os.path.dirname(__file__)
    onto_path = os.path.join(file_dir, 'Ontology Sheets', onto_version)

    # set Excel file into a dataframe
    try:
        role_df = pd.read_excel(onto_path, index_col=0,
                                sheet_name='Role Terms', usecols=[1, 2])
    except FileNotFoundError:
        raise ValueError

    # convert the dataframe into a dictionary
    role_dict = role_df.to_dict()['URI']

    # switch indices' and values' postions
    role_dict = {uri: role for role, uri in role_dict.items()}
    return role_dict


def organism_ontology(onto_version):
    """Read in organism ontology sheet from the sbol2excel/Ontology sheets folder.

    Reads in based on the onto_version supplied

    Args:
        onto_version (string): the name of the file in the Ontology Sheets
                            folder to read in

    Raises:
        TypeError: The onto_version supplied is not a string
        ValueError: The onto_version supplied does not point to a file int the
                    Ontology Sheets folder

    Returns:
        dictionary: Dictionary of the organisms of the form
            {'txid': 'Species Name'}, e.g.
            {'22': 'Shewanella', '23': 'Shewanella colwelliana'}
    """
    if type(onto_version) is not str:
        raise TypeError

    file_dir = os.path.dirname(__file__)
    onto_path = os.path.join(file_dir, 'Ontology Sheets', onto_version)

    # set Excel file into a dataframe
    try:
        org_df = pd.read_excel(onto_path, index_col=0,
                               sheet_name='Organism Terms', usecols=[0, 1])
    except FileNotFoundError:
        raise ValueError

    # convert the dataframe into a dictionary based on the txid column
    org_dict = org_df.to_dict()['txid']

    # switch indices' and values' postions
    org_dict = {str(txid): org for org, txid in org_dict.items()}

    return org_dict


def prop_convert(predicate):
    """Take property urls and converts them into more human readable names.

    Args:
        prop (str): a url for a property, e.g. http://purl.org/dc/terms/title
                    or http://sbols.org/v2#type

    Returns:
        prop: the updated more human readable prop (may be unchanged depending
                on the original input)
    """
    col_names = {
        'http://sbols.org/v2': 'sbol',
        'http://www.w3.org/1999/02/22-rdf-syntax-ns': 'rdf',
        'http://www.w3.org/2000/01/rdf-schema': 'rdfs',
        'http://wiki.synbiohub.org/wiki/Terms/synbiohub': 'sbh',
        'OBI_0001617': 'obo'
    }
    ns_counter = 0

    col_vals = hf.get_col_name(predicate)
    if col_vals[0] in col_names:
        ns_counter += 1
        return col_names[col_vals[0]] + ':' + col_vals[-1]
    else:
        ns_counter += 1
        # col_names[col_vals[0]] = 'ns' + str(ns_counter)
        col_names[col_vals[0]] = 'ns' + str(ns_counter)
        return col_names[col_vals[0]] + ':' + col_vals[-1]
