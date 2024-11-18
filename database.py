import mysql.connector

databaseConnection = mysql.connector.connect(
    host="localhost",
    user="root",
    password="root",
    database="roulettegame"
)

database = databaseConnection.cursor()

database.execute(f"INSERT INTO login(username, password) VALUES (\"user_1\", \"securepassword\")")
database.execute(f"INSERT INTO data(username, money) VALUES (\"user_1\", 121300)")
database.execute(f"INSERT INTO bank(username, interest, amountTaken) VALUES (\"user_1\", 12, 543)")

database.execute(f"INSERT INTO login(username, password) VALUES (\"user_2\", \"securepassword\")")
database.execute(f"INSERT INTO data(username, money) VALUES (\"user_2\", 10000)")
database.execute(f"INSERT INTO bank(username, interest, amountTaken) VALUES (\"user_2\", 0, 0)")

database.execute(f"INSERT INTO login(username, password) VALUES (\"user_3\", \"securepassword\")")
database.execute(f"INSERT INTO data(username, money) VALUES (\"user_3\", 10000)")
database.execute(f"INSERT INTO bank(username, interest, amountTaken) VALUES (\"user_3\", 0, 0)")

database.execute(f"INSERT INTO login(username, password) VALUES (\"user_4\", \"securepassword\")")
database.execute(f"INSERT INTO data(username, money) VALUES (\"user_4\", 10000)")
database.execute(f"INSERT INTO bank(username, interest, amountTaken) VALUES (\"user_4\", 0, 0)")

database.execute(f"INSERT INTO login(username, password) VALUES (\"user_5\", \"securepassword\")")
database.execute(f"INSERT INTO data(username, money) VALUES (\"user_5\", 10000)")
database.execute(f"INSERT INTO bank(username, interest, amountTaken) VALUES (\"user_5\", 0, 0)")

database.execute(f"INSERT INTO login(username, password) VALUES (\"user_6\", \"securepassword\")")
database.execute(f"INSERT INTO data(username, money) VALUES (\"user_6\", 10000)")
database.execute(f"INSERT INTO bank(username, interest, amountTaken) VALUES (\"user_6\", 0, 0)")

database.execute(f"INSERT INTO login(username, password) VALUES (\"user_7\", \"securepassword\")")
database.execute(f"INSERT INTO data(username, money) VALUES (\"user_7\", 10000)")
database.execute(f"INSERT INTO bank(username, interest, amountTaken) VALUES (\"user_7\", 0, 0)")

database.execute(f"INSERT INTO login(username, password) VALUES (\"user_8\", \"securepassword\")")
database.execute(f"INSERT INTO data(username, money) VALUES (\"user_8\", 10000)")
database.execute(f"INSERT INTO bank(username, interest, amountTaken) VALUES (\"user_8\", 0, 0)")

database.execute(f"INSERT INTO login(username, password) VALUES (\"user_9\", \"securepassword\")")
database.execute(f"INSERT INTO data(username, money) VALUES (\"user_9\", 10000)")
database.execute(f"INSERT INTO bank(username, interest, amountTaken) VALUES (\"user_9\", 0, 0)")

database.execute(f"INSERT INTO login(username, password) VALUES (\"user_10\", \"securepassword\")")
database.execute(f"INSERT INTO data(username, money) VALUES (\"user_10\", 10000)")
database.execute(f"INSERT INTO bank(username, interest, amountTaken) VALUES (\"user_10\", 0, 0)")

databaseConnection.commit()
print("done")