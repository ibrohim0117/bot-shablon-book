import sqlite3 

def create_table():
    conn = sqlite3.connect('data/baza.db')
    curr = conn.cursor()
    curr.execute("""
CREATE TABLE IF NOT EXISTS users(
    id integer primary key autoincrement,
    username VARCHAR(25) UNIQUE,
    user_id UNIQUE,
    date DATE
                 )

""")
    
    curr.execute("""
    CREATE TABLE IF NOT EXISTS categores(
        id integer primary key autoincrement,
        name VARCHAR(50) UNIQUE,
        date DATE
                    )

""")
    
    curr.execute("""
    CREATE TABLE IF NOT EXISTS products(
        id integer primary key autoincrement,
        name VARCHAR(50) UNIQUE,
        price INT,
        image VARCHAR(300),
        category VARCHAR(25),
        date DATE
                    )

""")
    

    curr.execute("""
    CREATE TABLE IF NOT EXISTS orders(
        id integer primary key autoincrement,
        name VARCHAR(50),
        count INT,
        user_id INT,
        date DATE
                    )

""")
    
    
    conn.commit()
    conn.close()



     