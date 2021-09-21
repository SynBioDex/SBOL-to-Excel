import sbol2excel.converter as conv
import os
import requests

cwd = os.getcwd()



def callTest(cwd):
    """
    To test the fuctionality of the sbol2excel converter, run this funtion with
    the given SBOL file. The 'cwd' parameter has been given to you at the top.
    """

    sbol_doc_path = os.path.join(cwd, 'SBOL2Excel', 'tests', 'test_files',
                                'test_sbol.xml')
    output_path = os.path.join(cwd, 'test.xlsx')
    conv.converter(sbol_doc_path, output_path)

def callURI(URI, cwd):
    """
    To convert your own SBOL file into and Excel spreadsheet, insert your own URI as
    the first parameter. The 'cwd' parameter has been given to you at the top.
    """

    new_xml = 'myFile.xml'
    imported_xml = requests.get(URI)
    output_path_new_xml = os.path.join(cwd, 'SBOL2Excel', 'tests', 'test_files', 
                    new_xml)
    file = open(output_path_new_xml, "w")
    file.write(imported_xml.text)
    file.close()
    sbol_doc_path_new_xml = os.path.join(cwd, 'SBOL2Excel', 'tests', 'test_files', 
                    new_xml)
    output_path_excel = os.path.join(cwd, 'my_xml_to_excel.xlsx')
    conv.converter(sbol_doc_path_new_xml, output_path_excel)
