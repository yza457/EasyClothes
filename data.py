import sqlite3
from sqlite3 import Error
import os
import json

def create_db():
    try:
        conn = sqlite3.connect(os.getcwd() + "/wardrobe.db")
        create_table = """  CREATE TABLE IF NOT EXISTS wardrobe (
                                id integer PRIMARY KEY,
                                type integer NOT NULL,
                                name varchar(20)
                            ); """
        conn.execute(create_table)
    except Error as e:
        print(e)
    finally:
        if conn:
            conn.close()



if __name__ == '__main__':
    create_db()
    # with open(os.getcwd() + "/test.json", 'r') as f:
    #     test = json.load(f)
    #     print(test[-1]['Kernel'])