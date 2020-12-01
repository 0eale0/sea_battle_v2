'''
Основная логика
1. Растоновка кораблей
    1. защитное поле
    2. добавить или убрать корабль
2. Атака
----------------------
z - не изменяемая пустая клетка
-1 - пустая клетка в защитном поле
0 - пустая клетка
1 - пустая битая клетка(промах)
2 - корабль
3 - битый корабль
'''
battlefield = [
    [0, 0, 0, 0, 0, 0, 0, 0, 0, 0],
    [0, 0, 0, 0, 0, 0, 0, 0, 0, 0],
    [0, 0, 0, 0, 0, 0, 0, 0, 0, 0],
    [0, 0, 0, 0, 0, 0, 0, 0, 0, 0],
    [0, 0, 0, 0, 0, 0, 0, 0, 0, 0],
    [0, 0, 0, 0, 0, 0, 0, 0, 0, 0],
    [0, 0, 0, 0, 0, 0, 0, 0, 0, 0],
    [0, 0, 0, 0, 0, 0, 0, 0, 0, 0],
    [0, 0, 0, 0, 0, 0, 0, 0, 0, 0],
    [0, 0, 0, 0, 0, 0, 0, 0, 0, 0],
]
while True:
    coordinates = [int(i) for i in input('x/y and type: ').split()]
    x = coordinates[0]
    y = coordinates[1]
    type = coordinates[2]
    if cell == 'z':
        print('Невозможный ход')
    elif 0 < x < 9 and 0 < y < 9 and type == 1:
        battlefield[x][y] = 2
        battlefield[x - 1][y] = 'z'
        battlefield[x + 1][y] = 'z'
        battlefield[x][y - 1] = 'z'
        battlefield[x][y + 1] = 'z'
        battlefield[x + 1][y + 1] = 'z'
        battlefield[x + 1][y - 1] = 'z'
        battlefield[x - 1][y + 1] = 'z'
        battlefield[x - 1][y - 1] = 'z'


for i in battlefield:
    print(*i)
