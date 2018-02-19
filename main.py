import sqlite3

conn = sqlite3.connect('friend.db')

c = conn.cursor()
c.execute('select * from phrases')
all_rows = c.fetchall()
print(all_rows)










