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
    db = sqlite3.connect(os.getcwd() + "/wardrobe.db")    
    cursor = db.cursor()
    count = 0
    index = 0
    for eachitem in items:
        count = cursor.rowcount
        clothesNo = count+1
        nickname = eachitem['name']
        clothestype = eachitem['type']
        location = eachitem['location']
        cursor.execute('INSERT INTO wardrobe_table(id, type, name, location) VALUES(?,?,?,?)',(clothesNo,nickname, clothestype, location))
        index=index+1
    db.commit()


if __name__ == '__main__':
    if not os.path.exists("wardrobe.db"):
        create_db()
    items = [
        {
        "name": "Ford",
        "type": "Mustang",
        "location": "closet"
        },
        {
        "name": "aaa",
        "type": "ddd",
        "location": "ffff"
        }
    ]
    store_insert(items)
    # with open(os.getcwd() + "/test.json", 'r') as f:
    #     test = json.load(f)
    #     print(test[-1]['Kernel'])