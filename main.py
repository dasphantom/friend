import sqlite3

conn = sqlite3.connect('friend.db')
c = conn.cursor()

#1. opening and getting first user respons
print ("Hey")

while True:
    user_input = input()

    #terminate on request
    if user_input.lower() == 'bye':
        print("Cya")
        quit()


    #2. check if user input already exists and print possible output
    c.execute('''SELECT output FROM phrases
          WHERE lower(input)=?'''
          ,(user_input.lower(),))

    row = c.fetchone()


    try:
        print(row[0])

    #3. nothing found, we need to ask the user for an appropriate response
    except (TypeError):
        print("How to respond to that?")

        user_input2 = input()

        c.execute('''INSERT INTO phrases (input,output)
        VALUES (?,?)'''
        ,(user_input,user_input2))

        conn.commit()

        print("Thank you")