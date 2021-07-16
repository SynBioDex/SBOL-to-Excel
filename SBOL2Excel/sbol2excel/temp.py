import utils.converter as conv
import os


cwd = os.getcwd()
sbol_doc_path = os.path.join(cwd, 'SBOL2Excel', 'tests', 'test_files',
                             'test_sbol.xml')
output_path = os.path.join(cwd, 'test.xlsx')
conv.converter(sbol_doc_path, output_path)
