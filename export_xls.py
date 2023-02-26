import xlsxwriter
import sqlite3

def sql_data_to_list_of_dicts(path_to_db, select_query):
    """Returns data from an SQL query as a list of dicts."""
    try:
        con = sqlite3.connect(path_to_db)
        con.row_factory = sqlite3.Row
        data = con.execute(select_query).fetchall()
        unpacked_data = [{k: item[k] for k in item.keys()} for item in data]
        return unpacked_data
    except Exception as e:
        print(f"Failed to execute. Query: {select_query}\n with error:\n{e}")
        return []
    finally:
        con.close()
        

def get_books_data():
    query = "SELECT * FROM books"
    books_data = sql_data_to_list_of_dicts("e-library.db", query)
    books_data_to_one_dict = {
        "id":[item["id"] for item in books_data],
        "title":[item["title"] + "\n" for item in books_data], 
        "description":[item["description"] + "\n" for item in books_data], 
        "year":[item["year"] for item in books_data],
        "publisher":[item["publisher"] + "\n" for item in books_data],
        "link":[item["link"] + "\n" for item in books_data]
                        }
    return books_data_to_one_dict

def get_authors_data():
    query = "SELECT * FROM authors"
    authors_data = sql_data_to_list_of_dicts("e-library.db", query)
    authors_names_to_dict = {"name":[item["name"] + "\n" for item in authors_data]}
    return authors_names_to_dict


def get_genres_data():
    query = "SELECT * FROM genres"
    genres_data = sql_data_to_list_of_dicts("e-library.db", query)
    genres_names_to_dict = {"name":[item["name"] + "\n" for item in genres_data]}
    return genres_names_to_dict



def write_data_to_xlsx():
    workbook = xlsxwriter.Workbook("library.xlsx")
    worksheet = workbook.add_worksheet("My Library")
    data_of_books = get_books_data()
    data_of_authors = get_authors_data()
    data_of_genres = get_genres_data()
    
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
    
    worksheet.write_column(row, column, data_of_books['id'])
    worksheet.write_column(row, column + 1, data_of_books["title"])
    worksheet.write_column(row, column + 2, data_of_authors["name"])
    worksheet.write_column(row, column + 3, data_of_genres["name"])
    worksheet.write_column(row, column + 4, data_of_books["link"])
    worksheet.write_column(row, column + 5, data_of_books["year"])
    worksheet.write_column(row, column + 6, data_of_books["publisher"])
    worksheet.write_column(row, column + 7, data_of_books["description"])
    row +=1
    
    workbook.close()
