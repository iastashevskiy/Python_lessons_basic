#!/usr/bin/python3

"""
== Лото ==

Правила игры в лото.

Игра ведется с помощью специальных карточек, на которых отмечены числа, 
и фишек (бочонков) с цифрами.

Количество бочонков — 90 штук (с цифрами от 1 до 90).

Каждая карточка содержит 3 строки по 9 клеток. В каждой строке по 5 случайных цифр, 
расположенных по возрастанию. Все цифры в карточке уникальны. Пример карточки:

--------------------------
    9 43 62          74 90
 2    27    75 78    82
   41 56 63     76      86 
--------------------------

В игре 2 игрока: пользователь и компьютер. Каждому в начале выдается 
случайная карточка. 

Каждый ход выбирается один случайный бочонок и выводится на экран.
Также выводятся карточка игрока и карточка компьютера.

Пользователю предлагается зачеркнуть цифру на карточке или продолжить.
Если игрок выбрал "зачеркнуть":
	Если цифра есть на карточке - она зачеркивается и игра продолжается.
	Если цифры на карточке нет - игрок проигрывает и игра завершается.
Если игрок выбрал "продолжить":
	Если цифра есть на карточке - игрок проигрывает и игра завершается.
	Если цифры на карточке нет - игра продолжается.
	
Побеждает тот, кто первый закроет все числа на своей карточке.

Пример одного хода:

Новый бочонок: 70 (осталось 76)
------ Ваша карточка -----
 6  7          49    57 58
   14 26     -    78    85
23 33    38    48    71   
--------------------------
-- Карточка компьютера ---
 7 11     - 14    87      
      16 49    55 77    88    
   15 20     -       76  -
--------------------------
Зачеркнуть цифру? (y/n)

Подсказка: каждый следующий случайный бочонок из мешка удобно получать 
с помощью функции-генератора.

Подсказка: для работы с псевдослучайными числами удобно использовать 
модуль random: http://docs.python.org/3/library/random.html

"""


import random

def get_row_values():
	r = [random.randint(1,91) for i in range(0,5)]
	r.sort()
	for i in range (0, len(r) - 1):
		if r[i] == r[i+1]:
			r = [random.randint(1,91) for i in range(0,5)]
			r.sort()
	return r


def insert_blancks(row):
	for i in range (0,3):
		row.insert(random.randint(0,len(row)), '-')
	return row


def genetrate_card():
	
	row1 = get_row_values()
	row2 = get_row_values()
	row3 = get_row_values()
	
	for i in range (0, len(row2)):
		if row2[i] in row1:
			row2 = get_row_values()
	
	for i in range (0, len(row3)):
		if row3[i] in row1 or row2:
			row3 = get_row_values()

	used_values = [row1 + row2 + row3]

	row1 = insert_blancks(row1)
	row2 = insert_blancks(row2)
	row3 = insert_blancks(row3)


	card = [row1, row2, row3]
	return card, used_values

def generate_barrel(used = []):
	
	barrel_value = random.randint(1,91)
	while barrel_value in used:
		barrel_value = random.randint(1,91)

	used.append(barrel_value)
	return barrel_value, used



genetated = genetrate_card()
card = genetated[0]
used = genetated[1]

bar = generate_barrel()
used = bar[1]
print(card)
print (bar[0])