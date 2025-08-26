import csv

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

def make_template(this_section_number,film_title,film_director,film_year,film_running_time,text_section,choose_section,option_text_1,section_number_1,option_text_2,section_number_2,option_text_3,section_number_3):
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
  print('<TITLE>')
  print('  Section ' + this_section_number + ' - ' + film_title)
  print('</TITLE>')
  print('')
  print('<h2>' + film_title + '</h2>')
  print('<P>')
  print('<I>' + film_director + '</I>')
  print('<P>')
  print('<I>' + film_year + '</I>')
  print('<P>')
  print('<I>' + film_running_time + ' minutes</I>')
  print('<P>')
  print(text_section)
  print('<P>')
  print('<I>' + choose_section + '</I>')
  print('<P>')
  print('<UL>')
  print('  <LI><I>' + option_text_1 + '</I> - <A HREF="' + padded_section_number_1 + '.html">Turn to section ' + section_number_1 + '</A>')
  print('  <LI><I>' + option_text_2 + '</I> - <A HREF="' + padded_section_number_2 + '.html">Turn to section ' + section_number_2 + '</A>')
  print('  <LI><I>' + option_text_3 + '</I> - <A HREF="' + padded_section_number_3 + '.html">Turn to section ' + section_number_3 + '</A>')
  print('</UL>')

make_template(this_section_number,film_title,film_director,film_year,film_running_time,text_section,choose_section,option_text_1,section_number_1,option_text_2,section_number_2,option_text_3,section_number_3)
