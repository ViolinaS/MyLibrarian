from ebook_sql_db import books, authors, genres, author_genre_book, favorite
import tkinter as tk
import tkinter.messagebox

class MyLibrarian:
    def __init__(self):
        # creation of the root window
        self.main_window = tk.Tk()
        self.main_window.title("My Librarian")
        self.main_window.geometry("500x500")
        self.main_window.resizable(True, True)
        
        # creation of the main_window frame
        self.main_frame = tk.Frame(self.main_window, borderwidth=1, relief="ridge")
        self.main_frame.pack(fill=tk.BOTH, expand=True)
        
        
        __doc__ = """
        Creation of the Menu buttons
        """ 
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
        
        # create button Favorites
        self.favorites_button = tk.Button(self.main_frame, text="Favorites", command=self.favorites)
        self.favorites_button.pack(side=tk.TOP, fill=tk.X, padx=10, pady=5)
        
        # create button Help
        self.help_button = tk.Button(self.main_frame, text="Help", command=self.help)
        self.help_button.pack(side=tk.TOP, fill=tk.X, padx=10, pady=5)
        
        # create button Exit
        self.exit_button = tk.Button(self.main_frame, text="Exit", command=self.exit)
        self.exit_button.pack(side=tk.TOP, fill=tk.X, padx=10, pady=5)
        
        # run main loop
        tk.mainloop()
        
        # create self.add_book function
    def add_book(self):
        tk.messagebox.showinfo("Add New Book", "Enter the title of the book")
    
    # create self.delete_book function
    def delete_book(self):
        tk.messagebox.showinfo("Delete a Book", "Delete the title of the book")
    
    # create self.find_book function
    def find_book(self):
        tk.messagebox.showinfo("Find a Book", "Find the title of the book")
        
    # create self.book_shelf function
    def book_shelf(self):
        tk.messagebox.showinfo("Book's Shelf", "Book's shelf")
        
    # create self.favorites function
    def favorites(self):
        tk.messagebox.showinfo("Favorites", "Favorites")
    
    # create self.help function
    def help(self):
        tk.messagebox.showinfo("Help", "Help")
    
    # create self.exit function
    def exit(self):
        tk.messagebox.showinfo("Exit", "Exit")






if __name__ == "__main__":
    librarian = MyLibrarian()