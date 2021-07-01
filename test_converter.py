import utils.sbol2excel as se
import os


cwd = os.getcwd()
file_path_in = os.path.join(cwd, 'SBOL2Excel', 'tests', 'test_files',
                            'pichia_toolkit_KWK_v002.xml')
file_path_out = os.path.join(cwd, 'output_test.xlsx')

seqfile_inst = se.seqFile(file_path_in, file_path_out)
seqfile_inst.returnExcelChart()

# thing = [1, 2, 3]
# for col in range(1, len(thing)+1):
#     alpha = seqfile_inst.columnString(col)
#     print(alpha)