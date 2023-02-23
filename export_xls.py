import xlsxwriter
import os
from ebook_sql_db import path
import sqlite3

def get_data_from_books():
    try:
        global conn, cursor
        conn = sqlite3.connect(os.path.join(path, 'e-library.db'))
        conn.row_factory = sqlite3.Row
        cursor = conn.cursor()
        data_books = cursor.execute("SELECT * FROM books")
    except sqlite3.Error as e:
        print(e)
    
    rows = data_books.fetchone()
    books_data = {}
    for row in rows.keys():
        books_data[row] = rows[row]
        
    return books_data

def get_data_from_authors():
    try:
        data_authors = cursor.execute("SELECT * FROM authors")
    except sqlite3.Error as e:
        print(e)
        
    authors = data_authors.fetchone()
    authors_data = {}
    for author in authors.keys():
        authors_data[author] = authors[author]
    
    return authors_data

def get_data_from_genres():
    try:
        data_genres = cursor.execute("SELECT * FROM genres")
    except sqlite3.Error as e:
        print(e)
        
    genres = data_genres.fetchone()
    genres_data = {}
    for genre in genres.keys():
        genres_data[genre] = genres[genre]
    
    return genres_data
    
    
def write_data_to_xlsx():
    workbook = xlsxwriter.Workbook(os.path.join(path, 'library.xlsx'))
    worksheet = workbook.add_worksheet("My Library")
    data_of_books = get_data_from_books()
    data_of_authors = get_data_from_authors()
    data_of_genres = get_data_from_genres()
    
    row = 0
    column = 0
    
    worksheet.set_column("A:A", 10)
    worksheet.set_column("B:B", 30)
    worksheet.set_column("C:C", 30)
    worksheet.set_column("D:D", 20)
    worksheet.set_column("E:E", 50)
    worksheet.set_column("F:F", 10)
    worksheet.set_column("G:G", 20)
    worksheet.set_column("H:H", 50)
    
    worksheet.write(row, column, data_of_books['id'])
    worksheet.write(row, column + 1, data_of_books["title"])
    worksheet.write(row, column + 2, data_of_authors["name"])
    worksheet.write(row, column + 3, data_of_genres["name"])
    worksheet.write(row, column + 4, data_of_books["link"])
    worksheet.write(row, column + 5, data_of_books["year"])
    worksheet.write(row, column + 6, data_of_books["publisher"])
    worksheet.write(row, column + 7, data_of_books["description"])
    row +=1
    
    workbook.close()

library_info = write_data_to_xlsx()   
print(get_data_from_books())
print(get_data_from_authors())
print(get_data_from_genres())
