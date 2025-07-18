import sqlite3 

def insert_user(username, user_id, date):
    conn = sqlite3.connect('data/baza.db')
    curr = conn.cursor()
    query = "INSERT OR IGNORE INTO users(username, user_id, date) VALUES(?, ?, ?)"
    curr.execute(query, (username, user_id, date))
    conn.commit()
    conn.close()


def insert_category(name, date):
    conn = sqlite3.connect('data/baza.db')
    curr = conn.cursor()
    query = "INSERT INTO categores(name, date) VALUES(?, ?)"
    curr.execute(query, (name, date))
    conn.commit()
    conn.close()


def insert_book(name, price, image, date, category):
    conn = sqlite3.connect('data/baza.db')
    curr = conn.cursor()
    query = "INSERT INTO products(name, price, image, date, category) VALUES(?, ?, ?, ?, ?)"
    curr.execute(query, (name, price, image, date, category))
    conn.commit()
    conn.close()


def insert_order(name, count, user_id, date):
    conn = sqlite3.connect('data/baza.db')
    curr = conn.cursor()
    query = "INSERT INTO orders(name, count, user_id, date) VALUES(?, ?, ?, ?)"
    curr.execute(query, (name, count, user_id, date))
    conn.commit()
    conn.close()


def delete_book(name):
    conn = sqlite3.connect('data/baza.db')
    curr = conn.cursor()
    query = "DELETE FROM products WHERE name=?"
    curr.execute(query, (name, ))
    conn.commit()
    conn.close()