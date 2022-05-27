import sbol2excel.converter as conv
import os



direct = os.path.split(__file__)[0]
file_in = os.path.join(direct, 'tests', 'test_files', 'sbol_v7.xml')
file_out = os.path.join(direct, 'sbol_v7.xlsx')
print(file_in)
conv.converter(file_in, file_out)
