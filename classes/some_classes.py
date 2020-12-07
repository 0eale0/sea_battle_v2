from classes import constants_for_classes
from visual import emojies
from sqlalchemy import *
from sqlalchemy.orm import sessionmaker
from sqlalchemy.ext.declarative import declarative_base

engine = create_engine('sqlite:///database.db', echo=True)
Base = declarative_base(bind=engine)


#  Static functions for the classes


def create_ships():
    ships = []
    for size in constants_for_classes.size_of_ships:
        ships.append(Ship(size))
    return ships


#  Classes
class SeaBattleGame:
    def __init__(self, player_1, player_2):
        self.players_1 = player_1
        self.players_2 = player_2
        self.turn = 0  # can be 1 or 2

    def hit(self):
        pass


class Field(Base):
    """
    Create a field for the player with height and length. Next time planning to add some methods
    WATCH OUT THERE'S A NOT int(0), BUT str(0)
    """
    __tablename__ = 'Field'
    id = Column(Integer, primary_key=True)
    field_for_save = Column(UnicodeText, nullable=True)
    visual_field_for_save = Column(UnicodeText, nullable=True)

    def __init__(self,
                 height: int = constants_for_classes.height,
                 length: int = constants_for_classes.length):

        self.__field = [['0'] * length for i in range(height)]
        self.field_for_save = str(self.__field)

        self.__visual_field = [[emojies.zero] * length for i in range(height)]
        self.visual_field_for_save = str(self.__visual_field)

        s.add(self)
        s.commit()

    def __str__(self):
        result = [' '.join(x) for x in self.__visual_field]
        result = '\n'.join(result)
        return result

    def __setitem__(self, key, data):
        self.__field[key[0]][key[1]] = data

        if isinstance(data, Ship):  # only for objects emoji can't str(str)
            self.__visual_field[key[0]][key[1]] = str(data)
            return

        else:
            self.__visual_field[key[0]][key[1]] = emojies.dict_for_data[data]
        s.commit()

    def __getitem__(self, key):
        return self.__field[key[0]][key[1]]

    def __iter__(self):
        return iter(self.__field)


class Player(Base):
    __tablename__ = 'Player'
    id = Column(Integer, primary_key=True)
    t_id = Column(Integer)
    nickname = Column(UnicodeText, nullable=True)

    def __init__(self, t_id: int = 0, nickname: str = 'null'):
        self.field = Field()  # size can be changed
        self.t_id = t_id
        self.nickname = nickname
        self.ships = create_ships()
        s.add(self)
        s.commit()


class Ship(Base):
    __tablename__ = 'Ships'
    id = Column(Integer, primary_key=True)
    size = Column(Integer)
    orientation = Column(UnicodeText, nullable=True)
    already_place = Column(Boolean)
    hp = Column(Integer)
    __x = Column(Integer)
    __y = Column(Integer)
    booked_places_for_save = Column(UnicodeText, nullable=True)

    def __init__(self, size: int, orientation: str = 'vertical', ):
        """
        :param size:
        :param orientation: can be "vertical" or "horizontal" STANDARD == VERTICAL!
        """
        self.size = size
        self.orientation = orientation
        self.already_place = False
        self.hp = size
        self.__x = -1
        self.__y = -1
        self.booked_places = [[], []]  # all book coords. First list for the 'z', next for the objects like this:
        #  [[(1, 2), (3, 4)], [(0, 0)]] cords in example is random, bus is show structure
        self.booked_places_for_save = str(self.booked_places)
        s.add(self)
        s.commit()

    def __str__(self):
        return str(self.size)

    @property
    def x(self) -> int:
        return self.__x

    @x.setter
    def x(self, x_from_user) -> None:
        self.__x = x_from_user
        s.commit()

    @property
    def y(self) -> int:
        return self.__y

    @y.setter
    def y(self, y_from_user) -> None:
        self.__y = y_from_user
        s.commit()


sum_id = 'test'
Base.metadata.create_all()
Session = sessionmaker(bind=engine)
s = Session()
