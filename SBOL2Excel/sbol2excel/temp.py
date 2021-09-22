"""
This module serves as a caller to the others.

One the functions are called, your results will be properly output.
"""
import sbol2excel.converter as conv
import os
import requests

cwd = os.getcwd()


def callTest(cwd):
    """
    Run this function to test the converter.

    The 'cwd' parameter has been given to you at the top.
    """
    sbol_doc_path = os.path.join(
                    cwd,
                    'SBOL2Excel',
                    'tests',
                    'test_files',
                    'test_sbol.xml')
    output_path = os.path.join(cwd, 'test.xlsx')
    conv.converter(sbol_doc_path, output_path)


def callURI(URI, cwd):
    """
    Use this function to apply the converter to your own SBOL document.

    Your desired URI serves as the first parameter.

    The 'cwd' parameter has been given to you at the top.
    """
    new_xml = 'myFile.xml'
    imported_xml = requests.get(URI)
    output_path_new_xml = os.path.join(
                cwd,
                'SBOL2Excel',
                'tests',
                'test_files',
                new_xml)
    file = open(output_path_new_xml, "w")
    file.write(imported_xml.text)
    file.close()
    sbol_doc_path_new_xml = os.path.join(
            cwd,
            'SBOL2Excel', 'tests',
            'test_files',
            new_xml)

    output_path_excel = os.path.join(cwd, 'my_xml_to_excel.xlsx')
    conv.converter(sbol_doc_path_new_xml, output_path_excel)
