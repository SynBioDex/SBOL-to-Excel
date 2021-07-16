# run by typing 'pytest' into the terminal
# for more detailed output use 'pytest -v -s'
import pytest
import sbol2excel.helper_functions as hf
import pandas as pd


@pytest.mark.parametrize(
    'col_name, raising_err, expected', [
        (1, False, "A"),
        (27, False, "AA"),
        (2, False, "B"),
        ("1", False, "A"),
        (2.7, True, ValueError),
        ("2.7", True, TypeError),
        ("string", True, TypeError),
        (True, True, TypeError)
    ]
)
def test_col_to_num(col_name, raising_err, expected):
    if raising_err:
        with pytest.raises(expected):
            hf.col_to_num(col_name)
    else:
        assert hf.col_to_num(col_name) == expected


@pytest.mark.parametrize(
    'df, col_list, raising_err, expected', [
        (
            {'A': [1, 2], 'B': [3, 4], 'C': [5, 6], 'D': [7, 8]},
            ['A', 'B', 'C', 'D'], False,
            {'A': [1, 2], 'B': [3, 4], 'C': [5, 6], 'D': [7, 8]}
        ),
        (
            {'A': [1, 2], 'B': [3, 4], 'C': [5, 6], 'D': [7, 8]},
            ['A', 'B', 'D'], False,
            {'A': [1, 2], 'B': [3, 4], 'D': [7, 8], 'C': [5, 6]}
        ),
        (
            {'A': [1, 2], 'B': [3, 4], 'C': [5, 6], 'D': [7, 8]},
            ['D', 'A'], False,
            {'D': [7, 8], 'A': [1, 2], 'B': [3, 4], 'C': [5, 6]}
        ),
        (
            {'A': [1, 2], 'B': [3, 4], 'C': [5, 6], 'D': [7, 8]},
            ['A', 'F', 'C', 'D'], False,
            {'A': [1, 2], 'C': [5, 6], 'D': [7, 8], 'B': [3, 4]}
        ),
        (
            {'A': [1, 2], 'B': [3, 4], 'C': [5, 6], 'D': [7, 8]},
            ['F', 'G', 'H', 'I'], False,
            {'A': [1, 2], 'B': [3, 4], 'C': [5, 6], 'D': [7, 8]}
        ),
        (
            {'A': [1, 2], 'B': [3, 4], 'C': [5, 6], 'D':[7, 8]},
            ['D', 'G', 'D'], False,
            {'D': [7, 8], 'A': [1, 2], 'B': [3, 4], 'C': [5, 6]}
        ),
        (
            {'A': [1, 2], 'B': [3, 4], 'C': [5, 6], 'D':[7, 8]},
            ['G', 'G', 'D'], False,
            {'D': [7, 8], 'A': [1, 2], 'B': [3, 4], 'C': [5, 6]}
        ),
        ("string", ['F', 'G', 'H', 'I'], True, TypeError),
        (
            {'A': [1, 2], 'B': [3, 4], 'C': [5, 6], 'D':[7, 8]},
            "string", True, TypeError
        )
    ]
)
def test_reorder_col(df, col_list, raising_err, expected):
    try:
        df = pd.DataFrame(data=df)
    except ValueError:
        pass
    if raising_err:
        with pytest.raises(expected):
            hf.reorder_col(df, col_list)
    else:
        reordered_df = hf.reorder_col(df, col_list)
        assert reordered_df.to_dict(orient='list') == expected
