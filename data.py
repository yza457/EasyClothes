import sqlite3
from sqlite3 import Error
import os
import json

def create_db():
    try:
        conn = sqlite3.connect(os.getcwd() + "/wardrobe.db")
        create_table = """CREATE TABLE wardrobe_table ( 
            id integer PRIMARY KEY,
            type integer NOT NULL,
            name varchar(20),
            location varchar(50))"""
        conn.execute(create_table)
    except Error as e:
        print(e)
    finally:
        if conn:
            conn.close()

def store_insert(items):
    if not os.path.exists("wardrobe.db"):
        create_db()
    db = sqlite3.connect(os.getcwd() + "/wardrobe.db")    
    cursor = db.cursor()
    index = 0
    cursor.execute("SELECT COUNT (*) FROM wardrobe_table")
    count = cursor.fetchone()[0]
    # print("now rowcount is " + str(cursor.rowcount))
    # count = 0 if cursor.rowcount == -1 else cursor.rowcount
    clothesNo = count+1
    nickname = items['name']
    clothestype = items['type']
    location = items['location']
    # print((clothesNo, nickname, clothestype, location))
    cursor.execute('INSERT INTO wardrobe_table(id, type, name, location) VALUES(?,?,?,?)',(clothesNo, clothestype, nickname, location))
    db.commit()

def store_retrieve(input):
    # input = '[{"Type": 1}]'
    type_hash = {1: "Top", 2: "Bottom", 3: "Shoes"}
    try:
        conn = sqlite3.connect(os.getcwd() + "/wardrobe.db")
    except Error as e:
        print(e)
    # input_type = input[0]['type']
    # print(input_type)
    cur = conn.cursor()
    cur.execute("SELECT * FROM wardrobe_table WHERE type=?", (input,))
    rows = cur.fetchall()
    print(rows)
    ret = []
    for row in rows:
        dict_row = {}
        dict_row['name'] = row[2]
        dict_row['type'] = type_hash[row[1]]
        dict_row['location'] = row[3]
        # print(dict_row)
        ret.append(dict_row)
    # print(ret)
    return ret    

def test():
    print("this is a test")


# if __name__ == '__main__':
#     if not os.path.exists("wardrobe.db"):
#         create_db()
#     items = [   {"name": "Ford", "type": "Mustang", "location": "closet"}, 
#                 {"name": "aaa", "type": "ddd", "location": "ffff"},
#                 {"name": "Ford2", "type": "Mustang", "location": "closet2"}]
#     store_insert(items)
#     # store_insert(items)
#     store_retrieve(items)
#     # with open(os.getcwd() + "/test.json", 'r') as f:
#     #     test = json.load(f)
#     #     print(test[-1]['Kernel'])