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
battlefield = [
    [0, 2, 2, 0, 1, 2, 3, 2, 2, 0],
    [0, 0, 1, 0, 1, 0, 1, 1, 1, 0],
    [0, 2, 3, 0, 1, 1, 1, 3, 1, 0],
    [0, 0, 0, 0, 1, 0, 1, 1, 1, 0],
    [0, 0, 0, 0, 0, 0, 0, 0, 0, 0],
    [0, 0, 0, 'z', 'z', 'z', 0, 0, 0, 0],
    [0, 0, 0, 'z', 2, 'z', 0, 0, 0, 0],
    [0, 0, 0, 'z', 2, 'z', 0, 0, 0, 0],
    [0, 0, 0, 'z', 'z', 'z', 0, 0, 0, 0],
    [0, 0, 0, 0, 0, 0, 0, 0, 0, 0],
]
move = 0
# потом сделаю проверку на отсутствие кораблей у противника и добавлю в while
while move != 100:
    coordinates = [int(i) for i in input('x/y: ').split()]
    x = coordinates[0]
    y = coordinates[1]
    if 0 <= x <= 9 and 0 <= y <= 9:
        if battlefield[x][y] % 2 == 0:
            battlefield[x][y] += 1
            for i in battlefield:
                print(*i)
            move += 1
        else:
            print('Невозможный ход')
    else:
        print('Неверно введены координаты')
