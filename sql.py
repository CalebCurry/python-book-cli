import sqlite3

conn = sqlite3.connect("books.db")
c = conn.cursor()

c.execute('''CREATE TABLE if not exists books(
            title TEXT,
            pages INTEGER
        )
'''
)

# c.execute("INSERT INTO books VALUES ('Are You My Mother?', 72)")
# conn.commit()

# books = [
#     ('The Digging-est Dog', 72),
#     ('Goodnight Moon', 31),
#     ('The Giving Tree', 66)
# ]

# c.executemany('INSERT INTO books VALUES (?,?)', books)
# conn.commit()

# c.execute("SELECT rowid, * FROM books")
# print(c.fetchall())

# c.execute("SELECT rowid, * FROM books LIMIT 1")
# print(c.fetchall())

# c.execute("DELETE FROM books WHERE rowid = ?", (1,))
# conn.commit()

# c.execute("SELECT * FROM books")
# print(c.fetchall())

# c.execute("UPDATE books SET pages=64 WHERE title = 'The Giving Tree'")
# conn.commit()

c.execute("SELECT * FROM books WHERE title = 'The Giving Tree'")
data = c.fetchone()
print(data)