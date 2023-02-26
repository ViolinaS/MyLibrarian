import sqlite3
from sqlite3 import Error
import os


__doc__ = """
This module contains the database and tables of the project.
"""
path = os.path.dirname(os.path.abspath(__file__))

class Database(object):
    def __init__(self):
        self.conn = None
        try:
            self.conn = sqlite3.connect('e-library.db')
            self.conn.row_factory = sqlite3.Row
            self.cursor = self.conn.cursor()
            self.cursor.execute('PRAGMA foreign_keys = ON')
            self.conn.commit()
        
        except Error as err:
            print(err)
            print('Failed to connect to the database')
            


# table --> authors
class Authors(Database):
    def __init__(self):
        Database.__init__(self)
        self.cursor.execute('''CREATE TABLE IF NOT EXISTS authors (
            id INTEGER PRIMARY KEY AUTOINCREMENT,
            name TEXT NOT NULL
        )''')
        self.conn.commit()
        

# table --> genres
class Genres(Database):
    def __init__(self):
        Database.__init__(self)
        self.cursor.execute('''CREATE TABLE IF NOT EXISTS genres (
            id INTEGER PRIMARY KEY AUTOINCREMENT,
            name TEXT NOT NULL            
        )''')
        self.conn.commit()

# table --> books
class Books(Database):
    def __init__(self):
        Database.__init__(self)
        self.cursor.execute('''CREATE TABLE IF NOT EXISTS books (
            id INTEGER PRIMARY KEY AUTOINCREMENT,
            title TEXT NOT NULL,
            year INTEGER,
            description TEXT,
            publisher TEXT,
            link TEXT NOT NULL,
            author_id INTEGER NOT NULL,
            genre_id INTEGER NOT NULL,
            FOREIGN KEY(author_id) REFERENCES authors(id) ON DELETE CASCADE,
            FOREIGN KEY(genre_id) REFERENCES genres(id) ON DELETE CASCADE
        )''')
        self.conn.commit()
        

# table --> favorite_shelf
class Favorite_shelf(Database):
    def __init__(self):
        Database.__init__(self)
        self.cursor.execute('''CREATE TABLE IF NOT EXISTS favorite_shelf (
            id INTEGER PRIMARY KEY AUTOINCREMENT,
            book_id INTEGER,
            FOREIGN KEY(book_id) REFERENCES books(id) ON DELETE CASCADE)''')
            
        self.conn.commit()  
        

books = Books()
authors = Authors()
genres = Genres()
favorite = Favorite_shelf()