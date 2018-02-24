import sqlite3

conn = sqlite3.connect('friend.db')
c = conn.cursor()

#1. opening and getting first user respons
print ("Hey")

while True:
    user_input = input()

    #2. check if user input already exists and print possible output
    c.execute('''SELECT output FROM phrases
          WHERE input=?'''
          ,(user_input,))

    row = c.fetchone()

    try:
        print(row[0])

    except (TypeError):
        print("weird")












