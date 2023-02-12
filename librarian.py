import tkinter
from tkinter import ttk
from tkinter import filedialog
from tkinter import messagebox
import sqlite3
from ebook import books, author_genre_book, authors, favorite, genres


class Librarian:
    def __init__(self):
        # create the main window
        self.main_window = tkinter.Tk()
        self.main_window.title("Library Management System")
        
        # layout main window content
        self.__build_main_window()

        # start the main loop
        tkinter.mainloop()

    # build the main window
    def __build_main_window(self):
        # create prompt label for user
        self.__create_prompt_label()

        # Listbox widget frame layout
        self.__build_listbox_frame()

        # create quit button
        self.__create_quit_button()

    # create prompt label for user
    def __create_prompt_label(self):
        self.prompt_label = tkinter.Label(
            self.main_window, text="Welcome to the Library Management System")
        self.prompt_label.grid(row=0, column=0, columnspan=2)
        self.prompt_label.config(font=("Helvetica", 12))
        self.prompt_label.pack(side='top', padx='5', pady='5')

    # Listbox and Scrollbar widgets frame layout
    def __build_listbox_frame(self):
        self.listbox_frame = tkinter.Frame(self.main_window)
        

        self.__setup_listbox()  # setup listbox widget

        # create scrollbar for listbox widget elements
        self.__create_scrollbar()

        # fill listbox widget by books titles
        self.__fill_listbox()

        # pack listbox widget frame
        self.listbox_frame.pack(side='top', padx='5', pady='5')

    # create a listbox widget to display book titles on the screen
    def __setup_listbox(self):
        # creation of listbox widget
        self.listbox = tkinter.Listbox(
            self.listbox_frame, selectmode=tkinter.SINGLE, height=10)

        # bind widget Listbox to a callback function
        self.listbox.bind('<<ListboxSelect>>', self.__get_details)

        # pack listbox widget
        self.listbox.pack(side='left', padx='5', pady='5')

    # create a vertical scrollbar widget for using with listbox widget
    def __create_scrollbar(self):
        self.scrollbar = tkinter.Scrollbar(
            self.listbox_frame, orient=tkinter.VERTICAL, command=self.listbox.yview)
        self.listbox.config(yscrollcommand=self.scrollbar.set)
        self.scrollbar.pack(side="right", fill=tkinter.Y)

    # display book titles on the listbox widget
    def __fill_listbox(self):
        for book in self.__get_books():
            self.listbox.insert(tkinter.END, book.title)

    # create quit button
    def __create_quit_button(self):
        self.quit_button = tkinter.Button(
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
        try:
            book_title = self.listbox.get(self.listbox.curselection()[0])
            self.__get_book_details(book_title)
            self.listbox.selection_clear(0, tkinter.END)    # ?????
            self.__display_details_books()
        
        except IndexError:
            pass
        
    # display details of selected book
    def __get_book_details(self, book_title):
        try:
            book = books.get_book(book_title)
            self.__display_book_details(book)
            messagebox.showinfo("Information: ", book.title)
        except sqlite3.OperationalError:
            messagebox.showerror(
                "Database Error", "Database connection error")
            

# main function
if __name__ == "__main__":
    librarian = Librarian()
    