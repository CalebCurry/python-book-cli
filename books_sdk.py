from book import Book
import sqlite3
import os.path

l = os.path.realpath(
    os.path.join(os.getcwd(), os.path.dirname(__file__)))

conn = sqlite3.connect(os.path.join(l, 'books.db'))

c = conn.cursor()

c.execute('''CREATE TABLE if not exists books(
            title TEXT,
            pages INTEGER
        )
'''
)
