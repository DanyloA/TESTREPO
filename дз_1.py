import random
file = open('Happy_new_year!.txt','w')
to_new_year = ''
first_word = ["Хорошего","Прекрастного","Удачного","Радостного","Щасливого","Лучшего","Кластного"]
second_word = ['следущего','нового','бычьего']
to_new_year += random.choice(first_word)
to_new_year += ' '
to_new_year += random.choice(second_word)
to_new_year += ' '
to_new_year += 'года!'
file.write(to_new_year)
file.close()
