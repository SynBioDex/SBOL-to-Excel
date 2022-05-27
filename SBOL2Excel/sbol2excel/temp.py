"""
This module serves as a caller to the others.

One the functions are called, your results will be properly output.
"""
import sbol2excel.converter as conv
import os


def callTest(file_name_in, file_name_out):
    """
    Run this function to test the converter.

    The 'cwd' parameter has been given to you at the top.
    """
    sbol_doc_path = os.path.join(
        cwd,
        'sbol2excel',
        'tests',
        'test_files',
        'rep_parts.xml')
    # enter code for class
    output_path = os.path.join(cwd, 'sbol2excel', 'tests', 'test_files', 'seed_out.xlsx')
    conv.converter(sbol_doc_path, output_path)


cwd = os.getcwd()
print(cwd)
callTest(cwd)
