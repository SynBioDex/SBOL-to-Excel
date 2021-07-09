# run by typing 'pytest' into the terminal
# for more detailed output use 'pytest -v -s'
import pytest
import utils.ontology_methods as om

# @pytest.mark.parametrize(
#     'prop, raising_err, expected', [
#         ("http://sbols.org/v2#type", False, 'types'),
#         ("http://purl.org/dc/terms/title", False, 'title'),
#         ("http://purl.obolibrary.org/obo/OBI_0001617", False, 'OBI_0001617'),
#         ("https://wiki.synbiohub.org/wiki/Terms/synbiohub#sourceOrganism",
#          False, 'sourceOrganism'),
#         ("http://purl.org/dc/terms/description", False, 'description'),
#         (76868, True, ValueError)
#     ]
# )
# def test_seqFile_prop_convert(prop, raising_err, expected):
#     seq_file_obj = s_e.seqFile('file_path_in', 'output_path')
#     if raising_err:
#         with pytest.raises(expected):
#             seq_file_obj.prop_convert(prop)
#     else:
#         assert seq_file_obj.prop_convert(prop) == expected
