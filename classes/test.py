import constants_for_classes
# from visual import emojies
from sqlalchemy import *
from sqlalchemy.orm import sessionmaker
from sqlalchemy.ext.declarative import declarative_base

engine = create_engine('sqlite:///database.db', echo=True)
Base = declarative_base(bind=engine)


def save_add(name_class):
    s.add(name_class)
    s.commit()


class Field(Base):
    """
    Create a field for the player with height and length. Next time planning to add some methods
    WATCH OUT THERE'S A NOT int(0), BUT str(0)
    """
    __tablename__ = 'Field'
    id = Column(Integer, primary_key=True)
    field_for_save = Column(String)
    visual_field_for_save = Column(String)

    def __init__(self,
                 height=10,
                 length=10):
        self.__field = x = [['0'] * length for i in range(height)]
        self.field_for_save = str(x)
        # self.__visual_field = [[emojies.zero] * length for i in range(height)]
        # self.visual_field_for_save = str(self.__visual_field)

    '''def __str__(self):
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
        save_up()

    def __getitem__(self, key):
        return self.__field[key[0]][key[1]]

    def __iter__(self):
        return iter(self.__field)'''


sum_id = 'test'
Base.metadata.create_all()
Session = sessionmaker(bind=engine)
s = Session()
battle = Field(10)
battle2 = Field()
s.add_all([battle, battle2])
s.commit()
print(battle)
