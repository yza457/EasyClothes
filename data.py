import sqlite3
from sqlite3 import Error
import os
import json

def create_db():
    try:
        conn = sqlite3.connect(os.getcwd() + "/wardrobe.db")
    except Error as e:
        print(e)
    finally:
        if conn:
            conn.close()

if __name__ == '__main__':
    # create_db()
    with open(os.getcwd() + "/test.json", 'r') as f:
        test = json.load(f)
        print(test[0]['Name'])