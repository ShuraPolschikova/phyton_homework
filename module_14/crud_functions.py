import sqlite3


def initiate_products_db():
    connection = sqlite3.connect("Products.db")
    cursor = connection.cursor()
    cursor.execute('''
    CREATE TABLE IF NOT EXISTS Products(
    id INTEGER PRIMARY KEY,
    title TEXT NOT NULL,
    description TEXT,
    price INTEGER NOT NULL
    )
    ''')
    cursor.execute("CREATE INDEX IF NOT EXISTS idx_title ON Products (title)")
    connection.commit()

    def check_prod(prod_title, prod_descr, prod_price):
        check = cursor.execute("SELECT * FROM Products WHERE title = ?", (prod_title,))
        if check.fetchone() is None:
            cursor.execute(f'''
            INSERT INTO Products (title, description, price) VALUES('{prod_title}','{prod_descr}','{prod_price}')
            ''')
            connection.commit()

    check_prod("Слива", "я слива лиловая, спелая, садовая", 11)
    check_prod("Абрикос", "а я абрикос, на юге рос", 22)
    check_prod("Томат", "а я томат", 33)
    check_prod("Фруктовый сад", "вместе мы фруктовый сад", 66)
    connection.commit()


def initiate_users_db():
    connection = sqlite3.connect("Users.db")
    cursor = connection.cursor()
    cursor.execute('''
        CREATE TABLE IF NOT EXISTS Users(
        id INTEGER PRIMARY KEY,
        username TEXT NOT NULL,
        email TEXT NOT NULL,
        age INTEGER NOT NULL,
        balance INTEGER NOT NULL
        )
        ''')
    cursor.execute("CREATE INDEX IF NOT EXISTS idx_email ON Users (email)")
    connection.commit()
    connection.close()


def add_user(username, email, age, balance):
    connection = sqlite3.connect("Users.db")
    cursor = connection.cursor()
    cursor.execute(f'''INSERT INTO Users (username, email, age, balance) VALUES 
    ('{username}', '{email}', {age}, {balance})''')
    connection.commit()
    connection.close()


def is_included(username):
    connection = sqlite3.connect("Users.db")
    cursor = connection.cursor()
    cursor.execute("SELECT COUNT(*) FROM Users WHERE username = ?", (username,))
    count = cursor.fetchone()[0]
    connection.close()
    return count > 0


def get_all_products():
    connection = sqlite3.connect("Products.db")
    cursor = connection.cursor()
    cursor.execute("SELECT title, description, price FROM Products")
    products = cursor.fetchall()
    connection.close()
    return products
