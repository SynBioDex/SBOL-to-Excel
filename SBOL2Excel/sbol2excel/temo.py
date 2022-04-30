from rdflib import Graph
import os

cwd = os.getcwd()
sbol_doc_path = os.path.join(
        cwd,
        'sbol2excel',
        'tests',
        'test_files',
        'test_sbol.xml')
g = Graph()
g.parse(sbol_doc_path)