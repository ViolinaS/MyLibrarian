# "MY LIBRARIAN"

![SQLite](https://img.shields.io/badge/sqlite-%2307405e.svg?style=for-the-badge&logo=sqlite&logoColor=white) ![Python](https://img.shields.io/badge/python-3670A0?style=for-the-badge&logo=python&logoColor=ffdd54)
![Tkinter](https://img.shields.io/badge/TKINTER-9cf/?style=for-the-badge&color=9cf&logo=python)
![XLSX](https://img.shields.io/badge/-xlsxwriter-9cf/?style=for-the-badge&color=orange&logo=python)

## Small application with GUI to manage your electronic books collection as library

---

### Application fitures

DATABASE: [ebook_sql_db.py](https://github.com/ViolinaS/my-librarian/blob/main/ebook_sql_db.py)

* All information about e-books is stored in the SQLite database.
* There are 4 tables in the [database](https://github.com/ViolinaS/my-librarian/blob/main/ebook_sql_db.py): books, authors, favorite_shelf, genres.

Database relation mapping:

![SQLite](https://github.com/ViolinaS/my-librarian/blob/main/media/my-librarian.png)

* table books contains Book's: id, title, author_id, genre_id, year(of release), link as a filepath,
description, publisher.
* table authors contains Author's: id, name
* table genres contains Genre's: id, name
* table favorite_shelf contains id, book_id
