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
    
    conn.commit()
    conn.close()