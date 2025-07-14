import sqlite3 

def show_all_categores():
    conn = sqlite3.connect('data/baza.db')
    curr = conn.cursor()
    query = "SELECT name FROM categores"
    data = curr.execute(query, ).fetchall()
    return data


def show_all_book():
    conn = sqlite3.connect('data/baza.db')
    curr = conn.cursor()
    query = "SELECT name, price, image FROM products"
    data = curr.execute(query, ).fetchall()
    return data


def show_detail_book(name):
    conn = sqlite3.connect('data/baza.db')
    curr = conn.cursor()
    query = "SELECT name, price, image FROM products WHERE name=?"
    data = curr.execute(query, (name, )).fetchone()
    return data



# print(show_detail_book('Tib qonunlari'))

# for i in (show_all_book()):
#     print(i[0])


# for i in (show_all_categores()):
#     print(i[0])




