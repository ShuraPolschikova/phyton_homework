import sqlite3


connection = sqlite3.connect("not_telegram2.db")
cursor = connection.cursor()


cursor.execute('''
CREATE TABLE IF NOT EXISTS Users(
id INTEGER PRIMARY KEY,
username TEXT NOT NULL,
email TEXT NOT NULL,
age INTEGER,
balance INTEGER NOT NULL
)
''')
cursor.execute("CREATE INDEX IF NOT EXISTS idx_email ON Users (email)")

for i in range(1, 11):
    cursor.execute("INSERT INTO Users (username, email, age, balance) VALUES (?,?,?,?)",
                   (f"(User{i})", f"(example{i}@gmail.com)", 10*i, 1000))

cursor.execute("UPDATE Users SET balance = BALANCE - 500 WHERE id % 2 = 1")
cursor.execute("DELETE FROM Users WHERE id % 3 = 1")
cursor.execute("DELETE FROM Users WHERE id = 6")

cursor.execute("SELECT username, email, age, balance FROM Users")
result = cursor.fetchall()

for user in result:
    print(f"Имя: {user[0]} | Почта: {user[1]} | Возраст: {user[2]} | Баланс: {user[3]}")

cursor.execute("SELECT COUNT (*) FROM Users")
result1 = cursor.fetchone()
print(f"Общее количество записей базы данных: {result1}")

cursor.execute("SELECT SUM(balance) FROM Users")
result2 = cursor.fetchone()
print(f"Сумма всех балансов: {result2}")

cursor.execute("SELECT AVG(balance) FROM Users")
result3 = cursor.fetchone()
print(f"Средний баланс всех пользователей: {result3}")


connection.commit()
connection.close()
