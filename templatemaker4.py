import pandas as pd
import json

#with open('out.txt', 'w') as f:
#  print(mylist, file=f)

#new_data = {'col1': ['pagetext']}
#df = pd.DataFrame(new_data)

def padnumber(x):
  if isinstance(x,int):
    if x >= 0 and x <= 9:
      padded_version = '00' + str(x)
    elif x >= 10 and x <= 99:
      padded_version = '0' + str(x)
    elif x >= 100 and x <= 999:
      padded_version = str(x)
    else:
      padded_version = str(x)
  else:
    padded_version = str(x)
  return padded_version

my_df_col = []
for i in range(1,251):
  print(str(i))
  padded_this_section_number = padnumber(i)
  print(padded_this_section_number)
#  with open('cyof_files/txt/' + padded_this_section_number + '.txt', 'r') as f:
  file = 'cyof_files/txt/' + padded_this_section_number + '.txt'
  with open(file,'r',encoding='utf-8') as myinfile:
    lines = myinfile.read().splitlines()
    #for thisline in lines:
    #  print(thisline)
    thisline_json = json.dumps(lines)
    my_df_col.append(thisline_json)

new_data = {'text_section': my_df_col}
df = pd.DataFrame(new_data)
print(df)

#print(my_df_col)
df.to_csv('temptemp1.csv')



df2 = pd.read_csv('sample_list2b.csv')
df2['text_section'] = my_df_col

df2.to_csv('temptemp2.csv')
