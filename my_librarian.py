from ebook_sql_db import books, authors, genres, favorite
import tkinter as tk
from tkinter import ttk, filedialog, Event, messagebox


class MyLibrarian:
    __doc__ = """
    This class is designed to be used with the e-library.db
    """

    def __init__(self):
        # creation of the root window
        self.main_window = tk.Tk()
        self.main_window.title("My Librarian")
        self.main_window.geometry("500x500")
        self.main_window.resizable(True, True)
        
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
        self.new_book_window.geometry("500x500")
        self.new_book_window.resizable(True, True)
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
        self.filepath_entry_text.insert(tk.END, self.filepath_entry)
        
        
        # create ok button
        self.ok_button = tk.Button(self.new_book_frame, text="OK", command=self.save_book_to_db)
        self.ok_button.pack(side=tk.TOP, fill=tk.X, padx=10, pady=5)
        
        # create cancel button
        self.cancel_button = tk.Button(self.new_book_frame, text="Cancel", command=self.new_book_window.destroy)
        self.cancel_button.pack(side=tk.TOP, fill=tk.X, padx=10, pady=5)
        

    
        
    
    # def add_book_to_db(self):
        # __doc__ = """
        # This function is used to write a new book to the e-library.db
        # """
        
        # try:
            # filepath = self.filepath_entry
            # print(filepath)
            # books.cursor.execute("INSERT INTO books (title, author_id, genre_id, release_year, description,\
            # publisher, link) VALUES (%s, %s, %s, %s, %s, %s, %s)",
                        # (self.title_entry.get(), self.author_entry.get(), self.genre_entry.get(), self.release_year_entry.get(),
                        # self.description_entry.get("1.0", tk.END), self.publisher_entry.get(), filepath))
            # books.conn.commit()
            
        # except:
            # messagebox.showerror("Error", "Something went wrong")
            
    def save_book_to_db(self):
        __doc__ = """
        This function is used to confirm a new book to the e-library.db
        """
        
        self.new_book_window.destroy()
        messagebox.showinfo("Saved book", "Book saved successfully")

    # create self.delete_book function
    def delete_book(self):
        messagebox.showinfo("Delete a Book", "Delete the title of the book")
    
    # create self.find_book function
    def find_book(self):
        messagebox.showinfo("Find a Book", "Find the title of the book")
        
    # create self.book_shelf function
    def book_shelf(self):
        messagebox.showinfo("Book's Shelf", "Book's shelf")
        
    # create self.favorites function
    def favorites(self):
        messagebox.showinfo("Favorites", "Favorites")
    
    # create self.help function
    def help(self):
        messagebox.showinfo("Help", "Help")
    
    # create self.exit function
    def exit(self):
        messagebox.showinfo("Exit", "Exit")






if __name__ == "__main__":
    librarian = MyLibrarian()