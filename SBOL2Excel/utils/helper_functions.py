import pandas as pd


def col_to_num(col_ind):
    """Generates Excel Column Name String based on an intger input,
    E.g. 1 is A and 27 is AA.

    Args:
        col_ind (integer): Column index to use

    Raises:
        TypeError: if col_ind is boolean, or a string that cannot
                    be converted to an integer
        ValueError: if col_ind is a float but not an integer

    Returns:
        col_name (string): The excel column name (uppercase)
    """
    if type(col_ind) is bool:
        # if boolean raise typerror
        raise TypeError
    elif type(col_ind) is str:
        # if string try to convert to an int
        try:
            col_ind = int(col_ind)
        except TypeError:
            raise TypeError
        except ValueError:
            raise TypeError
    elif type(col_ind) is not int:
        # if not int raise value error
        raise ValueError

    # carry out conversion
    col_name = ""
    while col_ind > 0:
        col_ind, remainder = divmod(col_ind - 1, 26)
        col_name = chr(65 + remainder) + col_name
    return col_name


def reorder_col(df, col_list):
    """A function to reorder the columns of a pandas dataframe based on a
    list of column names. The intersection of the column list and the dataframe
    column names may be >=0. Any df columns found in the column list are
    reordered according to the order in the column list and are moved to the
    front. The rest of the columns maintain the same order.
    For example a dataframe: A, C, D, E, F with a column list E, A, G, H
    will lead to a new dataframe with the columns ordered: E, A, C, D, F

    Args:
        df (pandas dataframe): A pandas data frame to be reordered
                               based on col_list
        col_list (list): A list of column names which may or may not
                        overlap with the column names in df. The df
                        column order will be rearranged based on this list

    Raises:
        TypeError: if df is not a pandas data frame or col_list is not a list

    Returns:
        pandas dataframe: reordered pandas dataframe
    """

    # check inputs are expected types
    if type(df) != pd.core.frame.DataFrame:
        raise TypeError
    if type(col_list) != list:
        raise TypeError

    # create list of column names
    df_col_list = df.columns

    # ordered list of columns in data frame but not in given list
    df_col_unique = [elem for elem in df_col_list if elem not in col_list]

    # ordered list of columns in data frame and ordered list
    df_col_shared = [elem for elem in col_list if elem in df_col_list]

    # append columns unique to the dataframe to the ordered list of shared
    # columns
    new_col_list = df_col_shared + df_col_unique

    # return reordered dataframe
    return df[new_col_list]
