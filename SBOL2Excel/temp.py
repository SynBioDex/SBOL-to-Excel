import sbol2excel.converter as conv
import os
# import sbol2
# from rdflib import Graph



direct = os.path.split(__file__)[0]
file_in = os.path.join(direct, 'tests', 'test_files', 'cello_library.xml')
file_out = os.path.join(direct, 'cello.xlsx')
# sbol_doc = sbol2.Document()
# sbol_doc.read(file_in)

# g = Graph()
# g.parse(sbol_doc)

# print("HI")

conv.converter(file_in, file_out)

