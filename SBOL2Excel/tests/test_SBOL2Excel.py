# pytest -v -s
import utils.sbol2excel as s_e
import pytest
import os

file_dir = os.path.dirname(__file__)
test_files_path = os.path.join(file_dir, 'test_files')


@pytest.mark.parametrize(
    'prop, raising_err, expected', [
        ("http://sbols.org/v2#type", False, 'types'),
        ("http://purl.org/dc/terms/title", False, 'title'),
        ("http://purl.obolibrary.org/obo/OBI_0001617", False, 'OBI_0001617'),
        ("https://wiki.synbiohub.org/wiki/Terms/synbiohub#sourceOrganism", False, 'sourceOrganism'),
        ("http://purl.org/dc/terms/description", False, 'description'),
        (76868, True, ValueError)
    ]
)
def test_seqFile_prop_convert(prop, raising_err, expected):
    seq_file_obj = s_e.seqFile('file_path_in', 'output_path')
    if raising_err:
        with pytest.raises(expected):
            seq_file_obj.prop_convert(prop)
    else:
        assert seq_file_obj.prop_convert(prop) == expected

# class seqFile:
#     def __init__(self, document):
#         # global varibales for homespace, document, and sheet
#         self.homeSpace = 'http://sys-bio.org'
#         self.document = document
#         self.sheet = 'ontologies.xlsx'


# def test_seqClass():
#     x = s_e.seqFile(file_path_in, output_path)
#     assert x.document == file_path_expected
#     # assert x.sheet == 'ontologies.xlsx'
#     # assert x.homeSpace == 'http://sys-bio.org'


# def test_roleVariables():
#     x = s_e.seqFile('pichia_toolkit_KWK_v002.xml')
#     roleDictionary = x.roleVariables()
#     assert roleDictionary == {}
