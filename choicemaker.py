import pandas as pd


#with open('out.txt', 'w') as f:
#  print(mylist, file=f)



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

df = pd.read_csv('sample_list2.csv')

filmhash = {}
for index,row in df.iterrows():
  this_section_number = row['this_section_number']
  film_title = row['film_title']
  film_director = row['film_director']
  film_year = row['film_year']
  film_running_time = row['film_running_time']
  text_section = row['text_section']
  choose_section = row['choose_section']
  option_text_1 = row['option_text_1']
  section_number_1 = row['section_number_1']
  option_text_2 = row['option_text_2']
  section_number_2 = row ['section_number_2']
  option_text_3 = row['option_text_3']
  section_number_3 = row['section_number_3']
  wiki_link = row['wiki_link']
  imdb_link = row['imdb_link']
  tvtropes_link = row['tvtropes_link']
  filmhash[padnumber(this_section_number)] = film_title
#  print(this_section_number)
#  print(film_title)
#  print(film_director)
#  print(film_year)
#  print(film_running_time)
#  print(text_section)
#  print(choose_section)
#  print(option_text_1)
#  print(section_number_1)
#  print(option_text_2)
#  print(section_number_2)
#  print(option_text_3)
#  print(section_number_3)
  #make_template(this_section_number,film_title,film_director,film_year,film_running_time,text_section,choose_section,option_text_1,section_number_1,option_text_2,section_number_2,option_text_3,section_number_3,wiki_link,imdb_link,tvtropes_link)


for index,row in df.iterrows():
  this_section_number = row['this_section_number']
  film_title = row['film_title']
  film_director = row['film_director']
  film_year = row['film_year']
  film_running_time = row['film_running_time']
  text_section = row['text_section']
  choose_section = row['choose_section']
  option_text_1 = row['option_text_1']
  section_number_1 = row['section_number_1']
  option_text_2 = row['option_text_2']
  section_number_2 = row ['section_number_2']
  option_text_3 = row['option_text_3']
  section_number_3 = row['section_number_3']
  wiki_link = row['wiki_link']
  imdb_link = row['imdb_link']
  tvtropes_link = row['tvtropes_link']
  print('*****************************')
  print(padnumber(this_section_number))
  print(film_title)
  print('(' + padnumber(section_number_1) + '_' + filmhash[padnumber(section_number_1)] + ') | ')
  print('(' + padnumber(section_number_2) + '_' + filmhash[padnumber(section_number_2)] + ') | ')
  print('(' + padnumber(section_number_3) + '_' + filmhash[padnumber(section_number_3)] + ') | ')
  print('*****************************')
