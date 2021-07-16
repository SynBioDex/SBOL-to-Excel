# run by typing 'pytest' into the terminal
# for more detailed output use 'pytest -v -s'
import pytest
import sbol2excel.ontology_methods as om


@pytest.mark.parametrize(
    'prop, raising_err, expected', [
        ("http://sbols.org/v2#type", False, 'Types'),
        ("http://purl.org/dc/terms/title", False, 'Part Name'),
        ("http://purl.obolibrary.org/obo/OBI_0001617", False, 'OBI_0001617'),
        (
            "https://wiki.synbiohub.org/wiki/Terms/synbiohub#sourceOrganism",
            False, 'Source Organism'
        ),
        ("http://purl.org/dc/terms/description", False, 'Part Description'),
        (76868, True, ValueError)
    ]
)
def test_prop_convert(prop, raising_err, expected):
    if raising_err:
        with pytest.raises(expected):
            om.prop_convert(prop)
    else:
        assert om.prop_convert(prop) == expected


@pytest.mark.parametrize(
    'onto_version, raising_err, expected_error', [
        ('ontologies_v000.xlsx', False, 'NA'),
        ('ontologies_v002.xlsx', True, ValueError),
        ('thing', True, ValueError),
        (76868, True, TypeError)
    ]
)
def test_organism_ontology(onto_version, raising_err, expected_error,
                           org_onto_v001_expected):
    if raising_err:
        with pytest.raises(expected_error):
            om.organism_ontology(onto_version)
    else:
        assert om.organism_ontology(onto_version) == org_onto_v001_expected


@pytest.mark.parametrize(
    'onto_version, raising_err, expected_error', [
        ('ontologies_v000.xlsx', False, 'NA'),
        ('ontologies_v002.xlsx', True, ValueError),
        ('thing', True, ValueError),
        (76868, True, TypeError)
    ]
)
def test_role_ontology(onto_version, raising_err, expected_error,
                       role_onto_v001_expected):
    if raising_err:
        with pytest.raises(expected_error):
            om.role_ontology(onto_version)
    else:
        assert om.role_ontology(onto_version) == role_onto_v001_expected
