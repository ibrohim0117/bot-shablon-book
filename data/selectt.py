import sqlite3 

def show_all_categores():
    conn = sqlite3.connect('data/baza.db')
    curr = conn.cursor()
    query = "SELECT name FROM categores"
    data = curr.execute(query, ).fetchall()
    return data


# for i in (show_all_categores()):
#     print(i[0])




