import sqlite3


def initiate_db():
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


    def check_user(prod_title, prod_descr, prod_price):
        check_user = cursor.execute("SELECT * FROM Products WHERE title = ?", (prod_title,))
        if check_user.fetchone() is None:
            cursor.execute(f'''
            INSERT INTO Products (title, description, price) VALUES('{prod_title}','{prod_descr}','{prod_price}')
            ''')
            connection.commit()

    check_user("Слива", "я слива лиловая, спелая, садовая", 11)
    check_user("Абрикос", "а я абрикос, на юге рос", 22)
    check_user("Томат", "а я томат", 33)
    check_user("Фруктовый сад", "вместе мы фруктовый сад", 66)

    connection.commit()
    connection.close()


def get_all_products():
    connection = sqlite3.connect("Products.db")
    cursor = connection.cursor()
    cursor.execute("SELECT title, description, price FROM Products")
    products = cursor.fetchall()
    connection.close()
    return products
