dictionary = {'/start': 'Идёт поиск игры, ожидайте',
              'game_found': 'Противник найден игра началась',
              '/help': 'Такие-то правила'}

end_line_button_random = 'Рандомная расстановка'
end_line_button_ready = 'Готов'


def winner_text(nickname):
    text = f'Поздравляем, вы унизили {nickname}'
    return text


def looser_text(nickname):
    text = f'Сожалеем, вы были унижены {nickname}'
    return text


