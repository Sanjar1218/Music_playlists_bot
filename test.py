from tinydb import TinyDB, Query
from database import User

# db = TinyDB('data.json')
# print(db.tables())


db = User('sanjarbek')

table = db.create_or_get_pl('my musics')

table.insert({'id':'new asdf'})
print(db.all_pl())