import sbol2excel.converter as conv
import os


cwd = os.getcwd()
sbol_doc_path = os.path.join(cwd, 'SBOL2Excel', 'tests', 'test_files',
                             'test_sbol.xml')
output_path = os.path.join(cwd, 'test.xlsx')
conv.converter("https://dev.synbiohub.org/public/igem/BBa_E0240/1/sbol", output_path)
