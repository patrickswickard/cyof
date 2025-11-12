import pandas as pd
import re

"""Demo read lines from file"""
file = 'nextchoice3.txt'
with open(file,'r',encoding='utf-8') as myinfile:
  lines = myinfile.read().splitlines()
  for thisline in lines:
    #print(thisline)
    next
a = int(len(lines)/7)

data = {}
choice1_list = []
choice2_list = []
choice3_list = []

for i in range(a):
  thislist = []
  for j in range(7):
    line_number = (7*i + j)
    thiscontent = lines[line_number]
    thislist.append(thiscontent)
  choiceraw1 = thislist[4]
  choiceraw2 = thislist[5]
  choiceraw3 = thislist[6]
  choice1 = re.sub(r"^.*\|\s*","",choiceraw1)
  choice2 = re.sub(r"^.*\|\s*","",choiceraw2)
  choice3 = re.sub(r"^.*\|\s*","",choiceraw3)
  choice1_list.append(choice1)
  choice2_list.append(choice2)
  choice3_list.append(choice3)

data['choice1'] = choice1_list
data['choice2'] = choice2_list
data['choice3'] = choice3_list

dataframe = pd.DataFrame(data)

dataframe.to_csv('outchoice3.csv')
