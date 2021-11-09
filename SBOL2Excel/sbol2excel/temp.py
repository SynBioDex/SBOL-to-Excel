"""
This module serves as a caller to the others.

One the functions are called, your results will be properly output.
"""
import sbol2excel.helper_functions as hf
import os

cwd = os.getcwd()


def callTest(cwd):
    """
    Run this function to test the converter.

    The 'cwd' parameter has been given to you at the top.
    """
    sbol_doc_path = os.path.join(
        cwd,
        'tests',
        'test_files',
        'simple_library.nt')
    output_path = os.path.join(cwd, 'test.xlsx')
    hf.sbol_validation(sbol_doc_path, output_path)


callTest(cwd)
