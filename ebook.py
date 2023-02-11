import sqlite3
from sqlite3 import Error
import os


__doc__ = """
This module contains the databases of the project.
"""
path = os.path.dirname(os.path.abspath(__file__))

class Database(object):
    def __init__(self):
        self.conn = None
        self.cursor = None
        try:
            self.conn = sqlite3.connect(os.path.join(path, 'e-library.db'))
            self.conn.row_factory = sqlite3.Row
            self.cursor = self.conn.cursor()
            self.cursor.execute('PRAGMA foreign_keys = ON')
            self.conn.commit()
        
        except sqlite3.Error as err:
            print(err)
            print('Failed to connect to the database')
            
# create table books
class Books(Database):
    def __init__(self):
        Database.__init__(self)
        self.cursor.execute('''CREATE TABLE IF NOT EXISTS books (
            id INTEGER PRIMARY KEY AUTOINCREMENT,
            title TEXT NOT NULL,
            year INTEGER NOT NULL,
            description TEXT,
            publisher TEXT NOT NULL,
            link TEXT NOT NULL
        )''')
        self.conn.commit()
        
        
# create table authors
class Authors(Database):
    def __init__(self):
        Database.__init__(self)
        self.cursor.execute('''CREATE TABLE IF NOT EXISTS authors (
            id INTEGER PRIMARY KEY AUTOINCREMENT,
            name TEXT NOT NULL,
            books_id INTEGER NOT NULL,
            FOREIGN KEY(books_id) REFERENCES books(id)
        )''')
        self.conn.commit()
        
        
# create table genres
class Genres(Database):
    def __init__(self):
        Database.__init__(self)
        self.cursor.execute('''CREATE TABLE IF NOT EXISTS genres (
            id INTEGER PRIMARY KEY AUTOINCREMENT,
            name TEXT NOT NULL            
        )''')
        self.conn.commit()
        
# create table author_genre_book
class Author_Genre_Book(Database):
    def __init__(self):
        Database.__init__(self)
        self.cursor.execute('''CREATE TABLE IF NOT EXISTS author_genre_book (
            author_id INTEGER REFERENCES authors(id),
            book_id INTEGER REFERENCES books(id),
            genre_id INTEGER REFERENCES genres(id),
            CONSTRAINT pk_author_genre_book PRIMARY KEY (author_id, book_id, genre_id)
        )''')
        self.conn.commit()  
        

# create table favorite_shelf
class Favorite_shelf(Database):
    def __init__(self):
        Database.__init__(self)
        self.cursor.execute('''CREATE TABLE IF NOT EXISTS favorite_shelf (
            id INTEGER PRIMARY KEY AUTOINCREMENT,
            book_id INTEGER,
            FOREIGN KEY(book_id) REFERENCES books(id))''')
            
        self.conn.commit()  
        

books = Books()
authors = Authors()
genres = Genres()
author_genre_book = Author_Genre_Book()
favorite = Favorite_shelf()