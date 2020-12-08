from sqlalchemy import *
from sqlalchemy.orm import sessionmaker
from sqlalchemy.ext.declarative import declarative_base

engine = create_engine('sqlite:///database.db', echo=True)
Base = declarative_base(bind=engine)


class AddPlayer(Player):
    __tablename__ = 'Player'
    id = Column(Integer, primary_key=True)
    t_id = Column(Integer)
    nickname = Column(UnicodeText, nullable=True)

    def __init__(self, t_id: int = 0, nickname: str = 'null'):
        self.t_id = t_id
        self.nickname = nickname
        s.add(self)
        s.commit()


Base.metadata.create_all()
Session = sessionmaker(bind=engine)
s = Session()
