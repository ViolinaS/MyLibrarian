from ebook_sql_db import books, authors, genres, favorite
import tkinter as tk
from tkinter import filedialog, messagebox, PhotoImage
import sqlite3
from buttons import NegativeButton, PositiveButton
from export import write_data_to_xlsx
import os

path = os.path.dirname(os.path.abspath(__file__))
img_path = os.path.join(path + '/media/librarian.png')

class MyLibrarian:
    __doc__ = """
    This class is designed to be used with e-library.db as GUI.
    """

    def __init__(self):
        # creation of the root window
        self.main_window = tk.Tk()
        self.main_window.title("My Librarian")
        self.main_window.geometry("300x500")
        self.main_window.resizable(False, False)
        
        # creation of the main_window frame
        self.main_frame = tk.Frame(self.main_window, relief="ridge")
        self.main_frame.pack(fill=tk.BOTH, expand=True)
        
        self.bg = PhotoImage(file=img_path)
        
        # Show image using label
        self.img_label = tk.Label(self.main_frame, image=self.bg)
        self.img_label.place(x=0, y=0, relwidth=1, relheight=1)
        
        # Create image frame
        self.img_frame = tk.Frame(self.main_frame)
        self.img_frame.pack(pady=20)
        
        """Creation of Menu buttons in the root window""" 
    
        # button to add new book
        self.add_book_button = PositiveButton(self.main_frame, text="Add New Book", command=self.__add_book)
        self.add_book_button.pack(side=tk.TOP, fill=tk.X, padx=10, pady=5)
        
        # button to remove books
        self.delete_book_button = PositiveButton(self.main_frame, text="Delete Books", command=self.__delete_book)
        self.delete_book_button.pack(side=tk.TOP, fill=tk.X, padx=10, pady=10)
        
        # button to find books
        self.find_book_button = PositiveButton(self.main_frame, text="Find a Book", command=self.__find_book)
        self.find_book_button.pack(side=tk.TOP, fill=tk.X, padx=10, pady=10)
        
        # button Favorites
        self.favorites_button = PositiveButton(self.main_frame, text="Favorites", command=self.__favorites)
        self.favorites_button.pack(side=tk.TOP, fill=tk.X, padx=10, pady=10)
        
        # button Export all books to xlsx
        self.export_xlsx = PositiveButton(self.main_frame, text="Export to XLSX", command=self.__export_xlsx)
        #self.export_xlsx.configure(bg="IndianRed4")
        self.export_xlsx.pack(side=tk.TOP, fill=tk.X, padx=10, pady=10)
        
        # button Help
        self.help_button = PositiveButton(self.main_frame, text="Help", command=self.__get_help)
        self.help_button.pack(side=tk.TOP, fill=tk.X, padx=10, pady=10)
        
        # button Exit
        self.exit_button = PositiveButton(self.main_frame, text="Exit", command=self.main_window.destroy)
        self.exit_button.pack(side=tk.TOP, fill=tk.X, padx=10, pady=10)
                
        """run main loop"""
        tk.mainloop()
        
    # self.add_book function
    def __add_book(self):
        __doc__= """
        This function is used to prepare to add a new book to the e-library.db
        Function is called by the add_book_button. 
        It starts new window and creates menu entries with labels above them.
        """
        # building new window
        self.new_book_window = tk.Toplevel(self.main_window)
        self.new_book_window.title("Add New Book")
        self.new_book_window.geometry("300x600")
        self.new_book_window.resizable(False, False)
        self.new_book_window.transient(self.main_window)
        self.new_book_window.grab_set()
        
        # building new window frame
        self.new_book_frame = tk.Frame(self.new_book_window, borderwidth=1, 
                                    relief="ridge", bg="MistyRose4")
        self.new_book_frame.pack(fill=tk.BOTH, expand=True)
        
        # Book's Title entry with its label
        self.title_lable = tk.Label(self.new_book_frame, text="Book's title: ", 
                                    bg="MistyRose4")
        self.title_entry = tk.Entry(self.new_book_frame, bg="blanched almond",
                                    highlightbackground="blanched almond")
        self.title_lable.pack(side=tk.TOP, fill=tk.X, padx=10, pady=5)
        self.title_entry.pack(side=tk.TOP, fill=tk.X, padx=10, pady=5)
        
        # Book's Author entry with its label
        self.author_lable = tk.Label(self.new_book_frame, text="Author's name: ",
                                    bg="MistyRose4")
        self.author_entry = tk.Entry(self.new_book_frame, bg="blanched almond",
                                    highlightbackground="blanched almond")
        self.author_lable.pack(side=tk.TOP, fill=tk.X, padx=10, pady=5)
        self.author_entry.pack(side=tk.TOP, fill=tk.X, padx=10, pady=5)
        
        # Book's Genre entry with its label
        self.genre_lable = tk.Label(self.new_book_frame, text="Genre: ",
                                    bg="MistyRose4")
        self.genre_entry = tk.Entry(self.new_book_frame, bg="blanched almond",
                                    highlightbackground="blanched almond")
        self.genre_lable.pack(side=tk.TOP, fill=tk.X, padx=10, pady=5)
        self.genre_entry.pack(side=tk.TOP, fill=tk.X, padx=10, pady=5)
        
        # Book's Release year entry with its label
        self.release_year_lable = tk.Label(self.new_book_frame, text="Release year: ",
                                        bg="MistyRose4")
        self.release_year_entry = tk.Entry(self.new_book_frame, bg="blanched almond",
                                        highlightbackground="blanched almond")
        self.release_year_lable.pack(side=tk.TOP, fill=tk.X, padx=10, pady=5)
        self.release_year_entry.pack(side=tk.TOP, fill=tk.X, padx=10, pady=5)
        
        # Book's Description entry for Text with its label
        self.description_lable = tk.Label(self.new_book_frame, text="Description: ",
                                        bg="MistyRose4", highlightbackground="blanched almond")
        self.description_entry = tk.Text(self.new_book_frame, bg="blanched almond", wrap="word", width=500)
        self.description_lable.pack(side=tk.TOP, fill=tk.X, padx=10, pady=5)
        self.description_entry.pack(side=tk.TOP, fill=tk.X, padx=10, pady=5)
        
        #Scrollbar for the description entry
        self.description_scrollbar = tk.Scrollbar(self.description_entry, bg="blanched almond", width=14,
                                                activebackground="coral")
        self.description_scrollbar.pack(side=tk.RIGHT, fill=tk.Y)
        self.description_entry.config(yscrollcommand=self.description_scrollbar.set)
        self.description_scrollbar.config(command=self.description_entry.yview)
        
        # Book's Publisher entry with its label
        self.publisher_lable = tk.Label(self.new_book_frame, text="Publisher: ",
                                        bg="MistyRose4")
        self.publisher_entry = tk.Entry(self.new_book_frame, bg="blanched almond",
                                        highlightbackground="blanched almond")
        self.publisher_lable.pack(side=tk.TOP, fill=tk.X, padx=10, pady=5)
        self.publisher_entry.pack(side=tk.TOP, fill=tk.X, padx=10, pady=5)
        
        # Book's filepath on the file system
        self.filepath_lable = tk.Label(self.new_book_frame, text="Filepath to your book: ",
                                    bg="MistyRose4")
        self.filepath_lable.pack(side=tk.TOP, fill=tk.X, padx=10, pady=5)
        self.filepath_entry = filedialog.askopenfilename()
        self.filepath_entry_text = tk.Entry(self.new_book_frame, bg="blanched almond",
                                            highlightbackground="blanched almond")
        self.filepath_entry_text.pack(side=tk.TOP, fill=tk.X, padx=10, pady=5)
        self.filepath_entry_text.insert(tk.END, (self.filepath_entry))
        
        
        # create ok button
        self.ok_button = PositiveButton(self.new_book_frame, text="Ok", command=self.__save_book_to_db)
        self.ok_button.pack(side=tk.TOP, fill=tk.X, padx=10, pady=5)
        
        # create exit button
        self.cancel_button = NegativeButton(self.new_book_frame, text="QUIT", command=self.new_book_window.destroy)
        self.cancel_button.pack(side=tk.TOP, fill=tk.X, padx=10, pady=5)

            
    def __save_book_to_db(self):
        """
        This function is used to write and confirm a new book to the e-library.db
        """
        conn = None
        try:
            conn = sqlite3.connect("e-library.db")
            cursor = conn.cursor()
            cursor.execute("INSERT INTO authors (name) VALUES (?)", (self.author_entry.get(),))
            cursor.execute("INSERT INTO genres (name) VALUES (?)", (self.genre_entry.get(),))
            conn.commit()
        except sqlite3.Error as err:
            print(err, "Database error")
            messagebox.showerror("Error", "Author or Genre is not added")
        finally:
            if conn != None:
                conn.close()
        
        try:
            conn = sqlite3.connect("e-library.db")
            cursor = conn.cursor()
            cursor.execute("""SELECT id FROM authors WHERE name =?""", (self.author_entry.get(),)) 
            author_id = cursor.fetchone()[0]
            genre = cursor.execute("""SELECT id FROM genres WHERE name =?""", (self.genre_entry.get(),))
            genre_id = genre.fetchone()[0]
        except sqlite3.Error as err:
            print(err, "Database error")
            messagebox.showerror("Error", "Database error")
        finally:
            if conn is not None:
                conn.close()
            
        try:
            conn = sqlite3.connect("e-library.db")
            cur = conn.cursor()
            cur.execute("""
                                INSERT INTO books 
                                (title, year, description, publisher, link, author_id, genre_id)
                                VALUES (?, ?, ?, ?, ?, ?, ?)""",
                                    (self.title_entry.get(), self.release_year_entry.get(), 
                                    self.description_entry.get("1.0", tk.END), self.publisher_entry.get(), 
                                    self.filepath_entry_text.get(), (author_id), (genre_id),))
            conn.commit()
            
        except sqlite3.Error as err:
            print(err, "Database error")
            messagebox.showerror("Error", "Book is not added")
        finally:
            if conn != None:
                conn.close()
                    
        self.new_book_window.destroy()
        
    
        

    # create self.delete_book function
    def __delete_book(self):
        """
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
        self.delete_frame = tk.Frame(self.delete_window, borderwidth=1, relief="ridge", bg="MistyRose4")
        self.delete_frame.pack(fill=tk.BOTH, expand=True)
        
        # create listbox wiget for all books in the database
        self.listbox = tk.Listbox(self.delete_frame, bg="MistyRose4",
                                selectmode=tk.MULTIPLE, selectbackground="IndianRed4", 
                                selectforeground="blanched almond",
                                cursor="hand2", activestyle="none")
        self.listbox.pack(side=tk.TOP, fill=tk.BOTH, expand=True, padx=10, pady=5)
        
        # insert all books in the listbox from the database, table books
        choose_book = books.cursor.execute("""SELECT title FROM books""")
        result = choose_book.fetchall()
        for book in result:
            self.listbox.insert(tk.END, book[0])
        
        # create delete button
        self.delete_button = PositiveButton(self.delete_frame, text="Delete", command=self.__delete_this_book)
        self.delete_button.pack(side=tk.TOP, fill=tk.X, padx=10, pady=5)
        
        # create exit button
        self.cancel_button = NegativeButton(self.delete_frame, text="QUIT", command=self.delete_window.destroy)
        self.cancel_button.pack(side=tk.TOP, fill=tk.X, padx=10, pady=5)
        
    
    def __delete_this_book(self):
        __doc__ = """
        This function is used to delete selected book from the e-library.db
        """
        try:
            books.cursor.execute(
                "DELETE FROM books WHERE title =?", 
                (self.listbox.get(self.listbox.curselection()[0]),)
                )
            books.conn.commit()
            
        except sqlite3.Error as err:
            print(err, "Database error")
            messagebox.showerror("Error", "Book is not deleted")
        finally:
            books.conn.close()
        
            self.listbox.delete(self.listbox.curselection()[0])
        self.delete_window.destroy()

    # create self.find_book function
    def __find_book(self):
        __doc__ = """
        This function shows all books from the database in the one list. 
        This function is called by the find_book_button.      
        """
        # building new window
        self.search_window = tk.Toplevel(self.main_window, bg="MistyRose4")
        self.search_window.title("Let's find a book")
        self.search_window.geometry("300x500")
        self.search_window.resizable(False, False)
        self.search_window.transient(self.main_window)
        self.search_window.grab_set()
        
        # building new window frames
        self.search_frame_all_books = tk.Frame(self.search_window, 
                                            relief="ridge", bg="MistyRose4")
        self.search_frame_all_books.pack(fill=tk.BOTH, expand=True)
        
        # create listbox wiget for all books in the database
        self.listbox_all_books = tk.Listbox(self.search_frame_all_books, bg="MistyRose4",
                                    selectmode=tk.SINGLE, selectbackground="IndianRed4",
                                    selectforeground="blanched almond",
                                    cursor="hand2", activestyle="none")
        self.listbox_all_books.pack(side=tk.TOP, fill=tk.BOTH, expand=True, padx=10, pady=5)
        # create Scrollbar widget for listbox_all_books
        self.listbox_all_books_scroll = tk.Scrollbar(self.listbox_all_books, width=14,
                                            bg="blanched almond", activebackground="IndianRed4")
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
        self.open_book_button = PositiveButton(self.search_window, text="Show Book", command=self.__open_this_book_details)
        self.open_book_button.pack(side=tk.TOP, fill=tk.X, padx=10, pady=5)
        
        # create add book to favorites button
        self.save_favorites_button = PositiveButton(self.search_window, text="Add To Favorites",
                                            command=self.add_favorites)
        self.save_favorites_button.pack(side=tk.TOP, fill=tk.X, padx=10, pady=5)
        
        # create exit button
        self.cancel_button = NegativeButton(self.search_window, text="QUIT", command=self.search_window.destroy)
        self.cancel_button.pack(side=tk.TOP, fill=tk.X, padx=10, pady=5)
    
    
    # create self.open_this_book_details function
    def __open_this_book_details(self):
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
            messagebox.showerror("Error", err)
            
        try:
            authors.cursor.execute("""SELECT name FROM authors WHERE id =?""", (book_details[0][6],))
            author_of_book = authors.cursor.fetchall()
            author_name = author_of_book[0][0]
            print(author_name)
            
        except sqlite3.Error as err:
            print(err, "Database error")
            messagebox.showerror("Error", err)
            
        try:
            genres.cursor.execute("""SELECT name FROM genres WHERE id =?""", (book_details[0][7],))
            genre_of_book = genres.cursor.fetchall()
            genre_name = genre_of_book[0][0]
            print(genre_name)
            
        except sqlite3.Error as err:
            print(err, "Database error")
            messagebox.showerror("Error", err)
            
        self.display_book_details (title = book_details[0][1], description = book_details[0][3],
                        publisher = book_details[0][4], link = book_details[0][5], year=book_details[0][2], 
                        author = author_name, genre = genre_name)
        
        
    def display_book_details(self, title, link, publisher, description, year, author, genre):
        __doc__ = """
        This method is used to display information about selected book from the table "books"
        """
        self.book_details_window = tk.Toplevel(self.main_window, bg="MistyRose4")
        self.book_details_window.title("Book Details")
        self.book_details_window.geometry("300x500")
        self.book_details_window.resizable(False, False)
        self.book_details_window.transient(self.main_window)
        self.book_details_window.grab_set()
        
        self.book_details_frame = tk.Frame(self.book_details_window, relief="ridge", bg="MistyRose4")
        self.book_details_frame.pack(fill=tk.BOTH, expand=True, padx=10, pady=5)
                        
        # create text widget inside book_details_frame
        self.book_text_info = tk.Text(self.book_details_frame, wrap="char", bg="MistyRose4")
        self.book_text_info.pack(fill=tk.BOTH, side=tk.LEFT, expand=True)
        
        # create Scrollbar widget for book_text_info
        self.book_text_info_scroll = tk.Scrollbar(self.book_text_info, width=14, cursor="hand2",
                                            bg="blanched almond", activebackground="IndianRed4")
        self.book_text_info_scroll.pack(side=tk.RIGHT, fill=tk.Y)
        self.book_text_info.config(yscrollcommand=self.book_text_info_scroll.set)
        self.book_text_info_scroll.config(command=self.book_text_info.yview)
                
        book_details_dict = {"Title": title, "Link": link, "Publisher": publisher, 
                            "Description": description, "Release year": year, "Author": author, "Genre": genre}
                
        for key, value in book_details_dict.items():
            self.book_text_info.insert(tk.END, f"{key}: {value}\n")
        
        # create close button
        self.close_book_button = NegativeButton(self.book_details_window, text="Close Book Details", command=self.book_details_window.destroy)
        self.close_book_button.pack(side=tk.BOTTOM, fill=tk.BOTH, padx=10, pady=5)
        
    def add_favorites(self):
        """This function adds books to Favorites and updates the database for table Favorite_shelf"""
        
        fave_book_index = self.listbox_all_books.curselection()[0]
        fave_book = self.listbox_all_books.get(fave_book_index)
        try:
            books.cursor.execute("""SELECT id FROM books WHERE title=?""", (fave_book,))
            book_id = books.cursor.fetchone()[0]
            print(book_id)
            favorite.cursor.execute("""INSERT INTO favorite_shelf (book_id) VALUES (?);""", (book_id,))
            favorite.conn.commit()
    
        except sqlite3.Error as err:
            print(err, "Database error")
            messagebox.showerror("Error", err)
        
        finally:
            favorite.conn.close()
    
    
    # create self.favorites function
    def __favorites(self):
        """This function is used to show favorite books separately from others"""
        
        #create listbox with scrollbar in a new window
        self.favorites_window = tk.Toplevel(self.main_window, bg="MistyRose4")
        self.favorites_window.title("My Favorite Books")
        self.favorites_window.geometry("300x500")
        self.favorites_window.resizable(False, False)
        self.favorites_window.transient(self.main_window)
        self.favorites_window.grab_set()
        
        self.favorites_frame = tk.Frame(self.favorites_window, relief="ridge", bg="MistyRose4")
        self.favorites_frame.pack(fill=tk.BOTH, expand=True, padx=10, pady=5)
    
        self.favorites_list = tk.Listbox(self.favorites_frame, bg="MistyRose4", selectmode=tk.MULTIPLE,
                                        selectbackground="IndianRed4", selectforeground="blanched almond",
                                        cursor="hand2", activestyle="none")
        self.favorites_list.pack(side=tk.TOP, fill=tk.BOTH, expand=True, padx=10, pady=5)
        
        self.favorites_scroll = tk.Scrollbar(self.favorites_list, width=14, cursor="hand2",
                                            bg="blanched almond", activebackground="IndianRed4")
        self.favorites_scroll.pack(side=tk.RIGHT, fill=tk.Y)
        
        self.favorites_list.config(yscrollcommand=self.favorites_scroll.set)
        self.favorites_scroll.config(command=self.favorites_list.yview)
        
        # insert all books in the listbox from the database, table favorite_shelf
        
        try:
            fave_book_show = books.cursor.execute(
                """SELECT title, book_id FROM books 
                inner join favorite_shelf on favorite_shelf.book_id = books.id
                GROUP BY title""")
                                    
            fave_books_list = [n[0] for n in fave_book_show.fetchall()]
            for book in fave_books_list:
                self.favorites_list.insert(tk.END, book)
            print(fave_books_list)
        
        except sqlite3.Error as err:
            print(err, "Database error")
            messagebox.showerror("Error", err)
        
        # create delete favorites button
        self.delete_favorites_button = PositiveButton(self.favorites_window, text="Delete Favorites",
                                            command=self.__delete_favorites)
        self.delete_favorites_button.pack(side=tk.TOP, fill=tk.X, padx=10, pady=5)
        
        # create open fave book button
        self.open_fave_button = PositiveButton(self.favorites_window, text="Open",
                                                    command=self.__open_fave_book)
        self.open_fave_button.pack(side=tk.TOP, fill=tk.X, padx=10, pady=5)
        
        # create exit button
        self.cancel_favorites_button = NegativeButton(self.favorites_window, text="QUIT",
                                                    command=self.favorites_window.destroy)
        self.cancel_favorites_button.pack(side=tk.TOP, fill=tk.X, padx=10, pady=5)
        

    # create self.delete_favorites function
    def __delete_favorites(self):
        """This function deletes selected favorite books from the database, table favorite_shelf"""
        
        fave_book_index = self.favorites_list.curselection()[0]
        fave_book = self.favorites_list.get(fave_book_index)
        
        try:
            favorite.cursor.execute("""DELETE FROM favorite_shelf
                WHERE book_id in (SELECT id FROM books WHERE title=?);""", (fave_book,))
                
            favorite.conn.commit()

        except sqlite3.Error as err:
            print(err, "Database error")
            messagebox.showerror("Error", err)
        
        finally:
            favorite.conn.close()
        
        self.favorites_list.delete(fave_book_index)

    # create self.open_fave_book function
    def __open_fave_book(self):
        """This function shows details of selected book from Favorite list."""
        
        fave_book_index = self.favorites_list.curselection()[0]
        fave_book = self.favorites_list.get(fave_book_index)
                
        fave_book_details = sqlite3.connect("e-library.db")
        fave_book_details.row_factory = sqlite3.Row
        
        book_link = fave_book_details.execute("SELECT link FROM books WHERE title=?", 
                                            (fave_book,)).fetchone()[0]
        book_publisher = fave_book_details.execute("SELECT publisher FROM books WHERE title=?", 
                                                (fave_book,)).fetchone()[0]
        book_description = fave_book_details.execute("SELECT description FROM books WHERE title=?",
                                                    (fave_book,)).fetchone()[0]
        book_year = fave_book_details.execute("SELECT year FROM books WHERE title=?",
                                            (fave_book,)).fetchone()[0]
        book_author_id = fave_book_details.execute("SELECT author_id FROM books WHERE title=?", 
                                                (fave_book,)).fetchone()[0]
        book_genre_id = fave_book_details.execute("SELECT genre_id FROM books WHERE title=?", 
                                                (fave_book,)).fetchone()[0]
        book_author = fave_book_details.execute("SELECT name FROM authors WHERE id=?", 
                                                (book_author_id,)).fetchone()[0]
        book_genre = fave_book_details.execute("SELECT name FROM genres WHERE id=?",
                                            (book_genre_id,)).fetchone()[0]
        print(f"{book_link}, {book_publisher}, {book_description}, {book_year}, {book_author}, {book_genre}")
                                                        
        self.display_book_details(title = fave_book, link = book_link, publisher = book_publisher, 
                                description = book_description, year = book_year, 
                                author = book_author, genre = book_genre)
        fave_book_details.close()
    
    
    # create self.help function
    def __get_help(self):
        """This function is used to display the help information about the application."""
        
        with open("help.txt", "r") as f:
            text = f.read()
                
        self.help_window = tk.Toplevel(self.main_window, bg="MistyRose4")
        self.help_window.geometry("300x500")
        self.help_window.resizable(False, False)
        self.help_window.transient(self.main_window)
        self.help_window.title("Help")
        
        self.help_text = tk.Text(self.help_window, bg="MistyRose4", wrap="word")
        self.help_text.pack(fill=tk.BOTH, padx=10, pady=5, expand=True)
        self.help_text.insert(tk.END, text)
        self.help_text_close_button = NegativeButton(self.help_window, text="Close", 
                                                    command=self.help_window.destroy)
        self.help_text_close_button.pack(side=tk.BOTTOM, fill=tk.BOTH, padx=10, pady=5)
        
            
    # create self.export_xls function
    def __export_xlsx(self):
        """This function is used to export the data from the database to xlsx file.
        Data to be exported: book's title, book's link, book's publisher, book's description, 
        book's year, book's author = authors.name, book's genre = genres.name
        """
        write_data_to_xlsx()
        messagebox.showinfo("Export", "All books exported to xlsx file")        


if __name__ == "__main__":
    librarian = MyLibrarian()