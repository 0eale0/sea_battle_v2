class MyError(Exception):
    def __init__(self, text):
        self.txt = text


cant_place = MyError('Невозможно установить здесь корабль')
already_hit = MyError('Вы туда уже стреляли')
already_in_queue = MyError('Нет необходимости спамить')
