"""
This module serves as a caller to the others.

One the functions are called, your results will be properly output.
"""
import sbol2excel.converter as conv
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
        'cello_library.xml')
    # enter code for class
    output_path = os.path.join(cwd, 'out.xlsx')
    conv.converter(sbol_doc_path, output_path)


callTest(cwd)
