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

this_section_number = '1'
padded_this_section_number = padnumber(this_section_number)
film_title = 'Dogtooth'
film_director = 'Yorgos Lanthimos'
film_year = '2009'
film_running_time = '97'

text_section = 'This is text.'
choose_section = 'Time to choose something different:'

option_text_1 = 'Option 1'
option_text_2 = 'Option 2'
option_text_3 = 'Option 3'
section_number_1 = '39'
section_number_2 = '247'
section_number_3 = '248'
padded_section_number_1 = padnumber(section_number_1)
padded_section_number_2 = padnumber(section_number_2)
padded_section_number_3 = padnumber(section_number_3)

#this_section_number = '39'
#padded_this_section_number = padnumber(this_section_number)
#film_title = 'Häxan'
#film_director = 'Benjamin Christensen'
#film_year = '1922'
#film_running_time = '105'
#
#text_section = 'This is text.'
#choose_section = 'Time to choose something different:'
#
#option_text_1 = 'Option 1'
#option_text_2 = 'Option 2'
#option_text_3 = 'Option 3'
#section_number_1 = 'xyz'
#section_number_2 = 'xyz'
#section_number_3 = 'xyz'
#padded_section_number_1 = padnumber(section_number_1)
#padded_section_number_2 = padnumber(section_number_2)
#padded_section_number_3 = padnumber(section_number_3)

#this_section_number = '247'
#padded_this_section_number = padnumber(this_section_number)
#film_title = 'Tie Me Up! Tie Me Down!'
#film_director = 'Pedro Almodóvar'
#film_year = '1989'
#film_running_time = '97'
#
#text_section = 'This is text.'
#choose_section = 'Time to choose something different:'
#
#option_text_1 = 'Option 1'
#option_text_2 = 'Option 2'
#option_text_3 = 'Option 3'
#section_number_1 = 'xyz'
#section_number_2 = 'xyz'
#section_number_3 = 'xyz'
#padded_section_number_1 = padnumber(section_number_1)
#padded_section_number_2 = padnumber(section_number_2)
#padded_section_number_3 = padnumber(section_number_3)

#this_section_number = '248'
#padded_this_section_number = padnumber(this_section_number)
#film_title = 'What Have I Done To Deserve This?'
#film_director = ' Pedro Almodóvar '
#film_year = '1984'
#film_running_time = '101'
#
#text_section = 'This is text.'
#choose_section = 'Time to choose something different:'
#
#option_text_1 = 'Option 1'
#option_text_2 = 'Option 2'
#option_text_3 = 'Option 3'
#section_number_1 = 'xyz'
#section_number_2 = 'xyz'
#section_number_3 = 'xyz'
#padded_section_number_1 = padnumber(section_number_1)
#padded_section_number_2 = padnumber(section_number_2)
#padded_section_number_3 = padnumber(section_number_3)

def make_template(this_section_number,film_title,film_director,film_year,film_running_time,text_section,choose_section,option_text_1,section_number_1,option_text_2,section_number_2,option_text_3,section_number_3,wiki_link,imdb_link,tvtropes_link):
#  with open('out.txt', 'w') as f:
#    print(mylist, file=f)
  this_section_number = this_section_number
  padded_this_section_number = padnumber(this_section_number)
  film_title = film_title
  film_director = film_director
  film_year = film_year
  film_running_time = film_running_time
  text_section = text_section
  choose_section = choose_section
  option_text_1 = option_text_1
  section_number_1 = section_number_1
  padded_section_number_1 = padnumber(section_number_1)
  option_text_2 = option_text_2
  section_number_2 = section_number_2
  padded_section_number_2 = padnumber(section_number_2)
  option_text_3 = option_text_3
  section_number_3 = section_number_3
  padded_section_number_3 = padnumber(section_number_3)
  wiki_link = wiki_link
  imdb_link = imdb_link
  tvtropes_link = tvtropes_link
  with open('cyof_files/' + padded_this_section_number + '.html', 'w') as f:
    print('<TITLE>',file=f)
    print('  Section ' + str(this_section_number) + ' - ' + str(film_title),file=f)
    print('</TITLE>',file=f)
    print('',file=f)
    print('<h2>' + str(film_title) + '</h2>',file=f)
    print('<P>',file=f)
    print('<img style="max-width:100%;height:auto;" src="img/' + padded_this_section_number + '.jpg">',file=f)
    print('<P>',file=f)
    print('<I>' + str(film_director) + '</I>',file=f)
    print('<P>',file=f)
    print('<I>' + str(film_year) + '</I>',file=f)
    print('<P>',file=f)
    print('<I>' + str(film_running_time) + ' minutes</I>',file=f)
    print('<P>',file=f)
    if not wiki_link == 'NONE':
      print('<A HREF="' + wiki_link + '"><I>Wikipedia link</I></a>',file=f)
      print('<P>',file=f)
    if not imdb_link == 'NONE':
      print('<A HREF="' + imdb_link + '"><I>IMDB link</I></a>',file=f)
      print('<P>',file=f)
    if not tvtropes_link == 'NONE':
      print('<A HREF="' + tvtropes_link + '"><I>TV Tropes link</I></a>',file=f)
      print('<P>',file=f)
    print(str(text_section),file=f)
    print('<P>',file=f)
    print('<I>' + str(choose_section) + '</I>',file=f)
    print('<P>',file=f)
    print('<UL>',file=f)
    print('  <LI><I>' + str(option_text_1) + '</I> - <A HREF="' + str(padded_section_number_1) + '.html">Turn to section ' + str(section_number_1) + '</A>',file=f)
    print('  <LI><I>' + str(option_text_2) + '</I> - <A HREF="' + str(padded_section_number_2) + '.html">Turn to section ' + str(section_number_2) + '</A>',file=f)
    print('  <LI><I>' + str(option_text_3) + '</I> - <A HREF="' + str(padded_section_number_3) + '.html">Turn to section ' + str(section_number_3) + '</A>',file=f)
    print('</UL>',file=f)

#make_template(this_section_number,film_title,film_director,film_year,film_running_time,text_section,choose_section,option_text_1,section_number_1,option_text_2,section_number_2,option_text_3,section_number_3)


print(df)
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
  make_template(this_section_number,film_title,film_director,film_year,film_running_time,text_section,choose_section,option_text_1,section_number_1,option_text_2,section_number_2,option_text_3,section_number_3,wiki_link,imdb_link,tvtropes_link)
