# To be written at a later date
# # run by typing 'pytest' into the terminal
# # for more detailed output use 'pytest -v -s'
# import utils.converter as conv
# import pytest


# @pytest.mark.parametrize(
#     'col_name, raising_err, expected', [
#         (1, False, "A"),
#         (27, False, "AA"),
#         (2, False, "B"),
#         ("1", False, "A"),
#         (2.7, True, ValueError),
#         ("2.7", True, TypeError),
#         ("string", True, TypeError),
#         (True, True, TypeError)
#     ]
# )
# def test_converter(col_name, raising_err, expected):
#     if raising_err:
#         with pytest.raises(expected):
#             hf.col_to_num(col_name)
#     else:
#         assert hf.col_to_num(col_name) == expected