import tkinter as tk
from tkinter import ttk
from tkinter import filedialog
from tkinter import messagebox
import sqlite3
from ebook import books, author_genre_book, authors, favorite, genres


__doc__ = """
This class is designed to be used with the e-library.db
"""


class Librarian:
    def __init__(self):
        # creation of the main window for the application
        self.main_window = tk.Tk()
        self.main_window.title("Library Management System")
        
        # layout main window content
        self.__build_main_window()

        # start the main loop
        tk.mainloop()

    # building the main window
    def __build_main_window(self):
        # prompt label for user
        self.__create_prompt_label()

        # Listbox widget frame layout
        self.__build_listbox_frame()

        # quit button
        self.__create_quit_button()

    # creation of prompt label for user
    def __create_prompt_label(self):
        self.prompt_label = tk.Label(
            self.main_window, text="Choose a book")
        self.prompt_label.grid(row=0, column=0, columnspan=2)
        self.prompt_label.config(font=("Helvetica", 12))
        self.prompt_label.pack(side='top', padx='5', pady='5')

    # Listbox and Scrollbar widgets frame layout
    def __build_listbox_frame(self):
        self.listbox_frame = tk.Frame(self.main_window)
        self.__setup_listbox()  # setup listbox widget

        # create scrollbar for listbox widget elements
        self.__create_scrollbar()

        # fill listbox widget by books titles
        self.__fill_listbox()

        # pack listbox widget frame
        self.listbox_frame.pack()

    # create a listbox widget to display book titles on the screen
    def __setup_listbox(self):
        # creation of listbox widget
        self.listbox = tk.Listbox(
            self.listbox_frame, selectmode=tk.SINGLE, height=6)

        # bind widget Listbox to a callback function
        self.listbox.bind('<<ListboxSelect>>', self.__get_details)

        # pack listbox widget
        self.listbox.pack(side='left', padx='5', pady='5')

    # creation of a vertical scrollbar widget for using with listbox widget
    def __create_scrollbar(self):
        self.scrollbar = tk.Scrollbar(
            self.listbox_frame, orient=tk.VERTICAL)
        self.scrollbar.config(command=self.listbox.yview)
        self.listbox.config(yscrollcommand=self.scrollbar.set)
        self.scrollbar.pack(side="right", fill=tk.Y)

    # display book titles on the listbox widget
    def __fill_listbox(self):
        for book in self.__get_books():
            self.listbox.insert(tk.END, book)

    # create quit button
    def __create_quit_button(self):
        self.quit_button = tk.Button(
            self.main_window, text="Quit", command=self.main_window.destroy)
        self.quit_button.pack(side='top', padx='10', pady='5')

    # get list of books from table books
    def __get_books(self):
        books_list = []
        try:
            get_books = books.cursor.execute('SELECT * FROM books').fetchall()
            books_list = [book[0] for book in get_books]
            return books_list
        except sqlite3.OperationalError:
            messagebox.showerror(
                "Database Error", "Database connection error")
            return []
            
    # get details of selected book
    def __get_details(self, event):
        listbox_index = self.listbox.curselection()[0]
        selected_book = self.listbox.get(listbox_index)
            
        # request in the books table from e-library.db details about selected_book
        try:
            get_details = author_genre_book.cursor.execute(
                'SELECT * FROM author_genre_book WHERE book_id == ?',
                (selected_book,))
            results = get_details.fetchone()
            
            # display details about selected book
            self.__display_details(results)
        
        except sqlite3.OperationalError:
            messagebox.showerror(
                "Database Error", "Database connection error")
            return
        
        finally:
            if author_genre_book.connection != None:
                author_genre_book.connection.close()
            


# main function
if __name__ == "__main__":
    librarian = Librarian()
    