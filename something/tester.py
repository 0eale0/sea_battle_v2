import pickle
import base64
import _compat_pickle
from data_base.db import cursor, conn


class Test:
    def __init__(self, t_id):
        self.t_id = t_id
        self.list_of_ints = [1, 2, 3]


test = Test(2)

encoded = pickle.dumps(test)

encoded_64 = encoded.decode(encoding = 'utf-8')

print(encoded_64)

cursor.execute("insert into table sea+ values (:data)", sqlite3.Binary(pdata))
