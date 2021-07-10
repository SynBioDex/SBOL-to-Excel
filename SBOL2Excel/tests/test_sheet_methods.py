# run by typing 'pytest' into the terminal
# for more detailed output use 'pytest -v -s'
import pytest
import os
import pandas as pd
import utils.sheet_methods as sm


@pytest.mark.parametrize(
    'sbol_test_doc, raising_err, expected', [
        ('test_sbol.xml', False, 'use_fixture'),
        ("string", True, ValueError)
    ]
)
def test_sbol_to_df(sbol_test_doc, raising_err, expected,
                    org_onto_v001_expected, role_onto_v001_expected,
                    sbol_to_df_expected):

    file_dir = os.path.dirname(__file__)
    sbol_doc_path = os.path.join(file_dir, 'test_files', sbol_test_doc)

    if raising_err:
        with pytest.raises(expected):
            sm.sbol_to_df(sbol_doc_path, role_onto_v001_expected,
                          org_onto_v001_expected)
    else:
        df = sm.sbol_to_df(sbol_doc_path, role_onto_v001_expected,
                           org_onto_v001_expected)

        df_dict = df.to_dict(orient='list')

        if expected == 'use_fixture':
            # done this way as nan is not equal to itself
            # additionally, due to xml not having a fixed order rows can
            # be read in in a different order
            for key in df_dict:
                ls = set(df_dict[key])
                ls = {it for it in ls if pd.notna(it)}
                ls_expected = set(sbol_to_df_expected[key])
                ls_expected = {it for it in ls_expected if pd.notna(it)}
                assert ls == ls_expected
        else:
            assert df_dict == expected


@pytest.mark.parametrize(
    'df, output_template, raising_err, expected', [
        ('df', 'Output_Template_v001.xlsx', False, 'na'),
        ('thing', 'Output_Template_v001.xlsx', True, TypeError),
        ('df', 'Output_Template_v002.xlsx', True, ValueError)
    ]
)
def test_df_to_excel(df, output_template, raising_err, expected,
                     test_df):

    file_dir = os.path.dirname(__file__)
    output_path = os.path.join(file_dir, 'test_files', 'test.xlsx')

    if df == 'df':
        df = test_df

    if raising_err:
        with pytest.raises(expected):
            sm.df_to_excel(df, output_path, output_template)
    else:
        sm.df_to_excel(df, output_path, output_template)

        # read in where the output is expected to be
        # and check it is as expected
        expected = pd.read_excel(output_path, header=18, usecols=[0, 1, 2, 3])
        assert df.equals(expected)
