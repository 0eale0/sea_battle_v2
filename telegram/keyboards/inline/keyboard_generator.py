from aiogram.types import InlineKeyboardMarkup, InlineKeyboardButton
from classes import some_classes
from visual import emojies
from classes.constants_for_classes import length, height
from telegram.data.text_for_handlers import end_line_button_random, end_line_button_ready


# player_for_test = some_classes.Player()

def add_field_to_keyboard(player: some_classes.Player, keyboard, invisible=False):

    field_with_emoji = player.field.get_field_with_emoji(invisible=invisible)

    # Add invisible space for best vision in smartphones
    for field_line in field_with_emoji:
        for i in range(length):
            field_line[i] = f'  {field_line[i]}  '

    x = 0
    y = 0

    for field_line in field_with_emoji:
        line = []
        for cell in field_line:
            line.append(InlineKeyboardButton(text=cell, callback_data=f'{y} {x}'))
            x += 1
        for button in line:
            keyboard.insert(button)
        y += 1
        x = 0

    return keyboard


def get_actual_keyboard(player: some_classes.Player, invisible=False):
    keyboard = InlineKeyboardMarkup(row_width=length)

    keyboard = add_field_to_keyboard(player, keyboard, invisible)

    return keyboard


def get_keyboard_phase_2(player: some_classes.Player):
    keyboard = InlineKeyboardMarkup(row_width=length)
    keyboard = add_field_to_keyboard(player, keyboard)

    random = InlineKeyboardButton(text=end_line_button_random, callback_data='random')
    ready = InlineKeyboardButton(text=end_line_button_ready, callback_data='ready')

    keyboard.insert(random)
    keyboard.insert(ready)

    return keyboard

'''    
    keyboard_2 = InlineKeyboardMarkup(row_width=1)
    hello = InlineKeyboardButton(text='h', callback_data='cancel')
    
    keyboard_2.insert(hello)'''
