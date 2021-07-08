import sbol2excel as sb
import os
import pandas as pd

cwd = os.getcwd()
filepathin = os.path.join(cwd, 'SBOL2Excel','tests', 'test_files', 'pichia_toolkit_KWK_v002.xml')

print(filepathin)

d = {'col1': [1, 2], 'col2': [3, 4], 'Role':[5,6], 'Design Notes':[7,8]}
df = pd.DataFrame(data=d)

# print(df)

sb_obj = sb.seqFile(filepathin, 'output_path') # calling __init__
sb_obj.overarching()
# print(sb_obj.reorder_columns(df))

