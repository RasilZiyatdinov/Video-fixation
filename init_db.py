import sqlite3

connection = sqlite3.connect('C:\proj\CV\microblog\database.db')

cur = connection.cursor()

cur.execute("""
CREATE TABLE posts (
    id INTEGER PRIMARY KEY AUTOINCREMENT, 
    created TIMESTAMP NOT NULL DEFAULT CURRENT_TIMESTAMP, 
    title TEXT NOT NULL,
    image TEXT NOT NULL,
    full_image TEXT NOT NULL,
    content TEXT
);
""")

connection.commit()
connection.close()