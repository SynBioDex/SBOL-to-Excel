# run by typing 'pytest' into the terminal
# for more detailed output use 'pytest -v -s'
import pytest
import utils.column_methods as cm


@pytest.mark.parametrize(
    'prop_nm, raising_err, expected', [
        ('no_change', False, "fake_no_change"),
        ('role', False, "fake_role"),
        ('something_weird', False, "fake_no_change"),
        (7, True, TypeError)
    ]
)
def test_col_methods_initialise(prop_nm, raising_err, expected,
                                monkeypatch):
    sbol_doc = 'sbol_doc'
    role_dict = 'role_dict'
    org_dict = 'org_dict'
    prop_val = 'prop_val'

    def fake_no_change(self):
        self.test = "fake_no_change"
        return

    def fake_role(self):
        self.test = "fake_role"
        return

    monkeypatch.setattr(cm.col_methods, 'no_change', fake_no_change)
    monkeypatch.setattr(cm.col_methods, 'role', fake_role)

    if raising_err:
        with pytest.raises(expected):
            cm.col_methods(prop_nm, prop_val, sbol_doc, role_dict, org_dict)
    else:
        method_output = cm.col_methods(prop_nm, prop_val, sbol_doc, role_dict,
                                       org_dict)
        assert method_output.test == expected


@pytest.mark.parametrize(
    'prop_val, role_dict, raising_err, expected', [
        (
            'http://identifiers.org/so/SO:0000167',
            {'http://identifiers.org/so/SO:0000167': 'promoter'},
            False, "promoter"
        ),
        (
            'thing',
            {'http://identifiers.org/so/SO:0000167': 'promoter'},
            False, 'thing'
        ),
        (
            'http://identifiers.org/so/SO:0000167',
            'thing',
            False, 'http://identifiers.org/so/SO:0000167'
        ),
        (
            7,
            {'http://identifiers.org/so/SO:0000167': 'promoter'},
            False, 7
        )
    ]
)
def test_role(prop_val, role_dict, raising_err, expected):
    prop_nm = 'no_change'
    sbol_doc = 'sbol_doc'
    org_dict = 'org_dict'
    col_meth_obj = cm.col_methods(prop_nm, prop_val, sbol_doc, role_dict,
                                  org_dict)
    if raising_err:
        with pytest.raises(expected):
            col_meth_obj.role()
    else:
        col_meth_obj.role()
        assert col_meth_obj.prop_val == expected


@pytest.mark.parametrize(
    'prop_val, raising_err, expected', [
        (
            'http://www.biopax.org/release/biopax-level3.owl#DnaRegion',
            False, "DnaRegion"
        ),
        ('role', True, ValueError),
        (7, True, TypeError)
    ]
)
def test_types(prop_val, raising_err, expected):
    prop_nm = 'no_change'
    role_dict = 'role_dict'
    sbol_doc = 'sbol_doc'
    org_dict = 'org_dict'
    col_meth_obj = cm.col_methods(prop_nm, prop_val, sbol_doc, role_dict,
                                  org_dict)
    if raising_err:
        with pytest.raises(expected):
            col_meth_obj.types()
    else:
        col_meth_obj.types()
        assert col_meth_obj.prop_val == expected


# test source organism
@pytest.mark.parametrize(
    'prop_val, org_dict, raising_err, expected_prop, expected_dict', [
        (
            'https://identifiers.org/taxonomy:4932',
            {'4932': 'Saccharomyces cerevisiae'},
            False, 'Saccharomyces cerevisiae',
            {'4932': 'Saccharomyces cerevisiae'}
        ),
        (
            'https://identifiers.org/taxonomy:562',
            {'4932': 'Saccharomyces cerevisiae'},
            False, 'Escherichia coli', {'4932': 'Saccharomyces cerevisiae',
                                        '562': 'Escherichia coli'}
        ),
        (
            'thing',
            {'4932': 'Saccharomyces cerevisiae'},
            True, ValueError, 'NA'
        ),
        (
            7,
            {'4932': 'Saccharomyces cerevisiae'},
            True, TypeError, 'NA'
        ),
        (
            'https://identifiers.org/taxonomy:562',
            'thing',
            True, TypeError, 'NA'
        )
    ]
)
def test_source_organism(prop_val, org_dict, raising_err, expected_prop,
                         expected_dict):
    prop_nm = 'no_change'
    sbol_doc = 'sbol_doc'
    role_dict = 'role_dict'
    col_meth_obj = cm.col_methods(prop_nm, prop_val, sbol_doc, role_dict,
                                  org_dict)
    if raising_err:
        with pytest.raises(expected_prop):
            col_meth_obj.source_organism()
    else:
        col_meth_obj.source_organism()
        assert col_meth_obj.prop_val == expected_prop
        assert col_meth_obj.org_dict == expected_dict

# test target organism

# test sequence
# need test file to use (pichia??)
