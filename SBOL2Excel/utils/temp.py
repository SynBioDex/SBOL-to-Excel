import sbol2excel as sb
import os

cwd = os.getcwd()
filepathin = os.path.join(cwd, 'SBOL2Excel','tests', 'test_files', 'pichia_toolkit_KWK_v002.xml')

print(filepathin)

sb_obj = sb.seqFile(filepathin, 'output_path')
sb_obj.readDocChart()