'''
это не много, но это честная работа
-2 - не изменяемая пустая клетка
-1 - пустая клетка в защитном поле
0 - пустая клетка
1 - пустая битая клетка(промах)
2 - корабль
3 - битый корабль
'''
# пусть пока будет заданое поле, потом надо будет сделать чтоб игрок сам задовал
# не придирайся если где-то корабли стоят не по правилам
field = [[0] * 10 for i in range(10)]
x = 3
y = 3
size = 6
orientation = 'vertical'


for index in range(size):
    for i in range(-1, 2):
        for j in range(-1, 2):
            field[y + i][x + j] = 'z'

    field[y][x] = size
    y += 1

y = 3

for index in range(size):
    field[y][x] = size
    y += 1



for line in field:
    print(*line)