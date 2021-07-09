import pandas as pd


def role_ontology():
    # set Excel file into a dataframe
    df = pd.read_excel(self.sheet, index_col=0,
                       sheet_name=1, usecols=[1, 2])
    # convert the dataframe into a dictionary
    roleConvertDict = df.to_dict()
    # set dictionary indices and values (use column 'URI' in excel sheet)
    roleName = roleConvertDict['URI']
    # switch indices' and values' postions
    roleDictionary = {uri: role for role, uri in roleName.items()}
    return roleDictionary


def organism_ontology():
    # set Excel file into a dataframe
    df = pd.read_excel(self.sheet, index_col=0,
                       sheet_name=2, usecols=[0, 1])
    # convert the dataframe into a dictionary
    organismConvertDict = df.to_dict()
    # set dictionary indices and values (use column 'txid' in excel sheet)
    organismName = organismConvertDict['txid']
    # switch indices' and values' postions
    organismDictionary = {str(txid): organism for organism, txid in organismName.items()}
    return organismDictionary


def prop_convert(prop):
    if type(prop) is str:
        idx = prop.find('#')
        # if parsing conditions meet, append them into the
        # componentFeatures dictionary as necessary
        if idx >= 1:
            prop = prop[idx + 1:]
        if prop == 'type':
            prop = 'types'
        if prop == 'http://purl.org/dc/terms/title':
            prop = 'title'
        if prop == 'http://purl.org/dc/terms/description':
            prop = 'description'
        if prop == 'http://purl.obolibrary.org/obo/OBI_0001617':
            prop = 'OBI_0001617'
        return (prop)
    else:
        raise ValueError()