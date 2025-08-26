import csv

#this_section_number = '1'
#padded_this_section_number = '001'
#film_title = 'Dogtooth'
#film_director = 'Yorgos Lanthimos'
#film_year = '2009'
#film_running_time = '97'
#
#text_section = 'This is text.'
#choose_section = 'Time to choose something different:'
#
#option_text_1 = 'Option 1'
#option_text_2 = 'Option 2'
#option_text_3 = 'Option 3'
#section_number_1 = '39'
#section_number_2 = '247'
#section_number_3 = '248'
#padded_section_number_1 = '039'
#padded_section_number_2 = '247'
#padded_section_number_3 = '248'

#this_section_number = '39'
#padded_this_section_number = '039'
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
#padded_section_number_1 = 'xyz'
#padded_section_number_2 = 'xyz'
#padded_section_number_3 = 'xyz'

#this_section_number = '247'
#padded_this_section_number = '247'
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
#padded_section_number_1 = 'xyz'
#padded_section_number_2 = 'xyz'
#padded_section_number_3 = 'xyz'

this_section_number = '248'
padded_this_section_number = '248'
film_title = 'What Have I Done To Deserve This?'
film_director = ' Pedro Almodóvar '
film_year = '1984'
film_running_time = '101'

text_section = 'This is text.'
choose_section = 'Time to choose something different:'

option_text_1 = 'Option 1'
option_text_2 = 'Option 2'
option_text_3 = 'Option 3'
section_number_1 = 'xyz'
section_number_2 = 'xyz'
section_number_3 = 'xyz'
padded_section_number_1 = 'xyz'
padded_section_number_2 = 'xyz'
padded_section_number_3 = 'xyz'

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

