from ebook_sql_db import books, authors, genres, favorite
import tkinter as tk
from tkinter import ttk, filedialog, Event, messagebox
from tkinter.scrolledtext import ScrolledText
import sqlite3


class MyLibrarian:
    __doc__ = """
    This class is designed to be used with the e-library.db
    """

    def __init__(self):
        # creation of the root window
        self.main_window = tk.Tk()
        self.main_window.title("My Librarian")
        self.main_window.geometry("300x500")
        self.main_window.resizable(False, False)
        
        # creation of the main_window frame
        self.main_frame = tk.Frame(self.main_window, borderwidth=1, relief="ridge")
        self.main_frame.pack(fill=tk.BOTH, expand=True)
        
        
        """Creation of the Menu buttons in the root window""" 
        
        # button to add new book
        self.add_book_button = tk.Button(self.main_frame, text="Add New Book", command=self.add_book)
        self.add_book_button.pack(side=tk.TOP, fill=tk.X, padx=10, pady=5)
        
        # button to remove books
        self.delete_book_button = tk.Button(self.main_frame, text="Delete a Book", command=self.delete_book)
        self.delete_book_button.pack(side=tk.TOP, fill=tk.X, padx=10, pady=5)
        
        # button to find books
        self.find_book_button = tk.Button(self.main_frame, text="Find a Book", command=self.find_book)
        self.find_book_button.pack(side=tk.TOP, fill=tk.X, padx=10, pady=5)
        
        # button Book's Shelf
        self.book_shelf_button = tk.Button(self.main_frame, text="Book's Shelf", command=self.book_shelf)
        self.book_shelf_button.pack(side=tk.TOP, fill=tk.X, padx=10, pady=5)
        
        # button Favorites
        self.favorites_button = tk.Button(self.main_frame, text="Favorites", command=self.favorites)
        self.favorites_button.pack(side=tk.TOP, fill=tk.X, padx=10, pady=5)
        
        # button Help
        self.help_button = tk.Button(self.main_frame, text="Help", command=self.help)
        self.help_button.pack(side=tk.TOP, fill=tk.X, padx=10, pady=5)
        
        # button Exit
        self.exit_button = tk.Button(self.main_frame, text="Exit", command=self.main_window.destroy)
        self.exit_button.pack(side=tk.TOP, fill=tk.X, padx=10, pady=5)
        
        """run main loop"""
        tk.mainloop()
        
        # self.add_book function
    def add_book(self):
        __doc__= """
        This function is used to prepare to add a new book to the e-library.db
        Function is called by the add_book_button. 
        It starts new window and creates menu entries with labels above them.
        """
        # building new window
        self.new_book_window = tk.Toplevel(self.main_window)
        self.new_book_window.title("Add New Book")
        self.new_book_window.geometry("300x500")
        self.new_book_window.resizable(False, False)
        self.new_book_window.transient(self.main_window)
        self.new_book_window.grab_set()
        
        # building new window frame
        self.new_book_frame = tk.Frame(self.new_book_window, borderwidth=1, relief="ridge")
        self.new_book_frame.pack(fill=tk.BOTH, expand=True)
        
        # Book's Title entry with its label
        self.title_lable = tk.Label(self.new_book_frame, text="Book's title: ")
        self.title_entry = tk.Entry(self.new_book_frame)
        self.title_lable.pack(side=tk.TOP, fill=tk.X, padx=10, pady=5)
        self.title_entry.pack(side=tk.TOP, fill=tk.X, padx=10, pady=5)
        
        # Book's Author entry with its label
        self.author_lable = tk.Label(self.new_book_frame, text="Author's name: ")
        self.author_entry = tk.Entry(self.new_book_frame)
        self.author_lable.pack(side=tk.TOP, fill=tk.X, padx=10, pady=5)
        self.author_entry.pack(side=tk.TOP, fill=tk.X, padx=10, pady=5)
        
        # Book's Genre entry with its label
        self.genre_lable = tk.Label(self.new_book_frame, text="Genre: ")
        self.genre_entry = tk.Entry(self.new_book_frame)
        self.genre_lable.pack(side=tk.TOP, fill=tk.X, padx=10, pady=5)
        self.genre_entry.pack(side=tk.TOP, fill=tk.X, padx=10, pady=5)
        
        # Book's Release year entry with its label
        self.release_year_lable = tk.Label(self.new_book_frame, text="Release year: ")
        self.release_year_entry = tk.Entry(self.new_book_frame)
        self.release_year_lable.pack(side=tk.TOP, fill=tk.X, padx=10, pady=5)
        self.release_year_entry.pack(side=tk.TOP, fill=tk.X, padx=10, pady=5)
        
        # Book's Description entry for Text with its label
        self.description_lable = tk.Label(self.new_book_frame, text="Description: ")
        self.description_entry = tk.Text(self.new_book_frame, width=500, height=5)
        self.description_lable.pack(side=tk.TOP, fill=tk.X, padx=10, pady=5)
        self.description_entry.pack(side=tk.TOP, fill=tk.X, padx=10, pady=5)
        
        # Book's Publisher entry with its label
        self.publisher_lable = tk.Label(self.new_book_frame, text="Publisher: ")
        self.publisher_entry = tk.Entry(self.new_book_frame)
        self.publisher_lable.pack(side=tk.TOP, fill=tk.X, padx=10, pady=5)
        self.publisher_entry.pack(side=tk.TOP, fill=tk.X, padx=10, pady=5)
        
        # Book's filepath on the file system
        self.filepath_lable = tk.Label(self.new_book_frame, text="Filepath to your book: ")
        self.filepath_lable.pack(side=tk.TOP, fill=tk.X, padx=10, pady=5)
        self.filepath_entry = filedialog.askopenfilename()
        self.filepath_entry_text = tk.Entry(self.new_book_frame)
        self.filepath_entry_text.pack(side=tk.TOP, fill=tk.X, padx=10, pady=5)
        self.filepath_entry_text.insert(tk.END, (self.filepath_entry))
        
        
        # create ok button
        self.ok_button = tk.Button(self.new_book_frame, text="OK", command=self.save_book_to_db)
        self.ok_button.pack(side=tk.TOP, fill=tk.X, padx=10, pady=5)
        
        # create cancel button
        self.cancel_button = tk.Button(self.new_book_frame, text="Cancel", command=self.new_book_window.destroy)
        self.cancel_button.pack(side=tk.TOP, fill=tk.X, padx=10, pady=5)

            
    def save_book_to_db(self):
        __doc__ = """
        This function is used to write and confirm a new book to the e-library.db
        """
        
        try:
            authors.cursor.execute("INSERT INTO authors (name) VALUES (?)", (self.author_entry.get(),))
            authors.conn.commit()
        except sqlite3.Error as err:
            print(err, "Database error")
            messagebox.showerror("Error", "Author is not added")
        
        try:
            genres.cursor.execute("INSERT INTO genres (name) VALUES (?)", (self.genre_entry.get(),))
            genres.conn.commit()
        except sqlite3.Error as err:
            print(err, "Database error")
            messagebox.showerror("Error", "Genre is not added")
            
        try:            
            author = authors.cursor.execute("""SELECT id FROM authors WHERE name =?""", (self.author_entry.get(),)) 
            author_id = author.fetchone()[0]
            print(author_id)
            genre = genres.cursor.execute("""SELECT id FROM genres WHERE name =?""", (self.genre_entry.get(),))
            genre_id = genre.fetchone()[0]
            print(genre_id)
            
            books.cursor.execute("INSERT INTO books (title, year, description, publisher, link, author_id, genre_id)\
            VALUES (?, ?, ?, ?, ?, ?, ?)",
                                    (self.title_entry.get(), self.release_year_entry.get(), 
                                    self.description_entry.get("1.0", tk.END), self.publisher_entry.get(), 
                                    self.filepath_entry_text.get(), (author_id), (genre_id),))
            books.conn.commit()
            messagebox.showinfo("Saved book", "Book saved successfully")
        except sqlite3.Error as err:
            print(err, "Database error")
            messagebox.showerror("Error", "Book is not added")
                    
        self.new_book_window.destroy()
        
    
        

    # create self.delete_book function
    def delete_book(self):
        # create document
        __doc__ = """
        This function is used to prepare listbox with book titles from books table 
        for selection to delete. This function is called by the delete_book_button.      
        """
        
        # building new window
        self.delete_window = tk.Toplevel(self.main_window)
        self.delete_window.title("Choose book to delete")
        self.delete_window.geometry("300x500")
        self.delete_window.resizable(False, False)
        self.delete_window.transient(self.main_window)
        self.delete_window.grab_set()
        
        # building new window frame
        self.delete_frame = tk.Frame(self.delete_window, borderwidth=1, relief="ridge")
        self.delete_frame.pack(fill=tk.BOTH, expand=True)
        
        # create listbox wiget for all books in the database
        self.listbox = tk.Listbox(self.delete_frame)
        self.listbox.pack(side=tk.TOP, fill=tk.BOTH, expand=True)
        
        # insert all books in the listbox from the database, table books
        choose_book = books.cursor.execute("""SELECT title FROM books""")
        result = choose_book.fetchall()
        for book in result:
            self.listbox.insert(tk.END, book[0])
        
        # create delete button
        self.delete_button = tk.Button(self.delete_frame, text="Delete", command=self.delete_this_book)
        self.delete_button.pack(side=tk.TOP, fill=tk.X, padx=10, pady=5)
        
        # create cancel button
        self.cancel_button = tk.Button(self.delete_frame, text="Cancel", command=self.delete_window.destroy)
        self.cancel_button.pack(side=tk.TOP, fill=tk.X, padx=10, pady=5)
        
    
    
    def delete_this_book(self):
        __doc__ = """
        This function is used to delete selected book from the e-library.db
        """
        try:
            books.cursor.execute("DELETE FROM books WHERE title =?", (self.listbox.get(self.listbox.curselection()[0]),))
            books.conn.commit()
            messagebox.showinfo("Deleted book", "Book deleted successfully")
        except sqlite3.Error as err:
            print(err, "Database error")
            messagebox.showerror("Error", "Book is not deleted")
        
            self.listbox.delete(self.listbox.curselection()[0])
        self.delete_window.destroy()

    # create self.find_book function
    def find_book(self):
        # create document
        __doc__ = """
        This function is used to search books and authors from database. 
        This function is called by the find_book_button.      
        """
        # building new window
        self.search_window = tk.Toplevel(self.main_window)
        self.search_window.title("Let's find a book")
        self.search_window.geometry("300x500")
        self.search_window.resizable(False, False)
        self.search_window.transient(self.main_window)
        self.search_window.grab_set()
        
        # building new window frames
        self.search_frame_all_books = tk.Frame(self.search_window, borderwidth=1, relief="ridge")
        self.search_frame_all_books.pack(fill=tk.BOTH, expand=True)
        self.search_frame_all_authors = tk.Frame(self.search_window, borderwidth=1, relief="ridge")
        self.search_frame_all_authors.pack(fill=tk.BOTH, expand=True)
        self.search_frame_by_request = tk.Frame(self.search_window, borderwidth=1, relief="ridge")
        self.search_frame_by_request.pack(fill=tk.BOTH, expand=True)
        
        # create show button --> all books
        self.search_button_books = tk.Button(self.search_frame_all_books, text="Show all Books", 
                                    command=self.show_all_books)
        self.search_button_books.pack(side=tk.TOP, fill=tk.X, padx=10, pady=5)
        
        # create show button --> all authors
        self.search_button_authors = tk.Button(self.search_frame_all_authors, text="Show all Authors", command=self.show_all_authors)
        self.search_button_authors.pack(side=tk.TOP, fill=tk.X, padx=10, pady=5)
        
        # create label for search by request
        self.search_by_request_label = tk.Label(self.search_frame_by_request, 
                                                text="Search by request:\n Input Book's title or Author's name, genre or publisher: ")
        self.search_by_request_label.pack(side=tk.TOP, fill=tk.X, padx=10, pady=5)
        
        # create search by request entry
        self.search_by_request_entry = tk.Entry(self.search_frame_by_request, width=30)
        self.search_by_request_entry.pack(side=tk.TOP, fill=tk.X, padx=10, pady=5)
        
        # create search button --> by request
        self.search_button = tk.Button(self.search_frame_by_request, text="Search", command=self.search_by_request)
        
        # create cancel button
        self.cancel_button = tk.Button(self.search_frame_by_request, text="Cancel", command=self.search_window.destroy)
        self.cancel_button.pack(side=tk.TOP, fill=tk.X, padx=10, pady=5)
        
    
    def show_all_books(self):
        __doc__ = """
        This function is called by the show_all_books_button.
        Function creates a listbox with scrollbar to show all books in the base by title.
        """
        
        # create listbox wiget for all books in the database
        self.listbox_all_books = tk.Listbox(self.search_frame_all_books)
        self.listbox_all_books.pack(side=tk.TOP, fill=tk.BOTH, expand=True)
    
        # create Scrollbar widget for listbox_all_books
        self.listbox_all_books_scroll = tk.Scrollbar(self.listbox_all_books)
        self.listbox_all_books_scroll.pack(side=tk.RIGHT, fill=tk.Y)
        self.listbox_all_books.config(yscrollcommand=self.listbox_all_books_scroll.set)
        self.listbox_all_books_scroll.config(command=self.listbox_all_books.yview)
        
        try:
            book_details = books.cursor.execute("""SELECT title FROM books""")
            books_list = [n[0] for n in book_details.fetchall()]
            for book in books_list:
                self.listbox_all_books.insert(tk.END, book)
                
        except sqlite3.Error as err:
            print(err, "Database error")
            
        # create open book button
        self.open_book_button = tk.Button(self.search_frame_all_books, text="Show Book", command=self.open_this_book_details)
        self.open_book_button.pack(side=tk.TOP, fill=tk.X, padx=10, pady=5)
        
        # create close button for all books listbox
        self.close_book_button = tk.Button(self.search_frame_all_books, text="Close", 
                                        command=self.close_show_all_books)
        self.close_book_button.pack(side=tk.TOP, fill=tk.X, padx=10, pady=5)
        
        self.search_button_books.config(state=tk.DISABLED)
    
    # create self.open_this_book_details function
    def open_this_book_details(self):
        __doc__ = """
        This function is used to open information about selected book from the table "books"
        """
        listbox_book_index = self.listbox_all_books.curselection()[0]
        selected_book = self.listbox_all_books.get(listbox_book_index)
        try:
            books.cursor.execute("SELECT * FROM books WHERE title =?", (selected_book,))
            book_details = books.cursor.fetchall()
                    
        except sqlite3.Error as err:
            print(err, "Database error")
            messagebox.showerror("Error", "Database error")
            
        try:
            authors.cursor.execute("""SELECT name FROM authors WHERE id =?""", (book_details[0][6],))
            author_of_book = authors.cursor.fetchall()
            author_name = author_of_book[0][0]
            print(author_name)
            
        except sqlite3.Error as err:
            print(err, "Database error")
            messagebox.showerror("Error", "Database error")
            
        try:
            genres.cursor.execute("""SELECT name FROM genres WHERE id =?""", (book_details[0][7],))
            genre_of_book = genres.cursor.fetchall()
            genre_name = genre_of_book[0][0]
            print(genre_name)
            
        except sqlite3.Error as err:
            print(err, "Database error")
            messagebox.showerror("Error", "Database error")
            
        self.display_book_details (title = book_details[0][1], description = book_details[0][3],
                        publisher = book_details[0][4], link = book_details[0][5], year=book_details[0][2], 
                        author = author_name, genre = genre_name)
        
        
    def display_book_details(self, title, link, publisher, description, year, author, genre):
        __doc__ = """
        This method is used to display information about selected book from the table "books"
        """
        self.book_details_window = tk.Toplevel(self.main_window)
        self.book_details_window.title("Book Details")
        self.book_details_window.geometry("300x500")
        self.book_details_window.resizable(False, False)
        self.book_details_window.transient(self.main_window)
        self.book_details_window.grab_set()
        
        self.book_details_frame = tk.Frame(self.book_details_window, borderwidth=1, border=1, relief="ridge")
        self.book_details_frame.pack(fill=tk.BOTH, expand=True)
                        
        # create text widget inside book_details_frame
        self.book_text_info = tk.Text(self.book_details_frame, wrap="word")
        self.book_text_info.pack(fill=tk.BOTH, side=tk.LEFT, expand=True)
        
        book_details_dict = {"Title": title, "Link": link, "Publisher": publisher, 
                            "Description": description, "Release year": year, "Author": author, "Genre": genre}
                
        for key, value in book_details_dict.items():
            self.book_text_info.insert(tk.END, f"{key}: {value}\n")
        
        # create close button
        self.close_book_button = tk.Button(self.book_details_window, text="Close", 
                                        command=self.book_details_window.destroy)
        self.close_book_button.pack(side=tk.BOTTOM, fill=tk.BOTH)
        
        


    # create self.close_this_book function
    def close_show_all_books(self):
        __doc__ = """
        This function is called by self.close_book_button to close listbox with books, buttons of show_all_books()
        and return to previous state.
        """
        self.listbox_all_books.destroy()
        self.search_button_books.config(state=tk.NORMAL)
        self.open_book_button.destroy()
        self.close_book_button.destroy()
    
    # create self.book_shelf function
    def book_shelf(self):
        pass
        
    # create self.favorites function
    def favorites(self):
        pass
    
    # create self.help function
    def help(self):
        pass
    
    # create self.exit function
    def exit(self):
        pass






if __name__ == "__main__":
    librarian = MyLibrarian()