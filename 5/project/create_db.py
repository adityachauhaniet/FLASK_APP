import sqlite3

conn = sqlite3.connect('site.db')

cursor = conn.cursor()

cursor.execute('''
               CREATE TABLE IF NOT EXISTS users(
               id INTEGER PRIMARY KEY,
               name TEXT NOT NULL,
               email TEXT NOT NULL
               )
            ''')

conn.commit()
conn.close()
