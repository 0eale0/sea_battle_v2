from aiogram.types import InlineKeyboardMarkup, InlineKeyboardButton
from classes import some_classes
from visual import emojies


# player_for_test = some_classes.Player()
keyboard = InlineKeyboardMarkup(row_width=8)

field = [['  ' + emojies.fire + '  '] * 8 for i in range(12)]

x = 0
y = 0

for field_line in field:
    line = []
    for cell in field_line:
        line.append(InlineKeyboardButton(text=cell, callback_data=f'y: {y} x: {x}'))
        x += 1
    for button in line:
        keyboard.insert(button)
    y += 1
    x = 0

print(keyboard)

keyboard_2 = InlineKeyboardMarkup(row_width=1)
hello = InlineKeyboardButton(text='h', callback_data='cancel')

keyboard_2.insert(hello)

