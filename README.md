# "MY LIBRARIAN"

![SQLite](https://img.shields.io/badge/sqlite-%2307405e.svg?style=for-the-badge&logo=sqlite&logoColor=white) ![Python](https://img.shields.io/badge/python-3670A0?style=for-the-badge&logo=python&logoColor=ffdd54)
![Tkinter](https://img.shields.io/badge/TKINTER-9cf/?style=for-the-badge&color=9cf&logo=python)
![XLSX](https://img.shields.io/badge/-xlsxwriter-9cf/?style=for-the-badge&color=orange&logo=python)

## Small application with GUI to manage your electronic books collection as library

### Application fitures

>>![main_window](https://github.com/ViolinaS/my-librarian/blob/b2c88bda0244cde59dcbe1418a31009831afb3e2/media/main_window.png) ![book_details](https://github.com/ViolinaS/my-librarian/blob/b2c88bda0244cde59dcbe1418a31009831afb3e2/media/book_details.png)

**MENU**

* Add New Book
  * *Adds new books into library interface, inserts and commits changes into database by OK button.*
* Delete Books
  * *Deletes books from library interface, commits changes into database by OK button.*
* Find a Book
  * *Shows all current books in the database, lets to add books into Favorites and openes selected book details in separate window*
* Favorites
  * *Shows all books chosen as favorite previously in new window, lets to delete books from favorite list and commits changes to database, opens fave book details.*
* Export to XLSX
  * *Creates xlsx file from SQLite tables data, includes all books from database*
  * *Exports Book's: id, title, year(of release), description, publisher, link with filepath to the book, author's name, genre's name*

**DATABASE**

[ebook_sql_db.py](https://github.com/ViolinaS/my-librarian/blob/main/ebook_sql_db.py)

* All information about e-books is stored in the SQLite database.
* There are 4 tables in the [database](https://github.com/ViolinaS/my-librarian/blob/main/ebook_sql_db.py): books, authors, favorite_shelf, genres.

Database relations mapping:

![SQLite](https://github.com/ViolinaS/my-librarian/blob/c816f707e097f7741aff29a723896530545e4c60/media/my-librarian.png)

***

### Requirements >>>> [requirements.txt](https://github.com/ViolinaS/my-librarian/blob/bd6a3423db9abf075a6b3273fe6209b66f0cd6cc/requirements.txt)

### Launch [my-librarian.py](https://github.com/ViolinaS/my-librarian/blob/bd6a3423db9abf075a6b3273fe6209b66f0cd6cc/my_librarian.py) to run this application

### Database, tables, xlsx file are being created automatically upon run the application and using GUI first time.