

from db import conn, cursor


class Book: #a table
    def __init__(self, id, title, author, isbn):#our columns
        self.id = id
        self.title = title
        self.author = author
        self.isbn = isbn

    def __repr__(self):#string representation of an object
        return f"<Book {self.id} {self.title} {self.author} {self.isbn}>"
    
                 #creating methods that we use or execute on the table
    @classmethod
    def create_table(cls):
        sql = """
            CREATE TABLE IF NOT EXISTS Books (
                id INTEGER PRIMARY KEY AUTOINCREMENT,
                title TEXT NOT NULL,
                author TEXT NOT NULL,
                isbn TEXT NOT NULL UNIQUE
            )
        """
        cursor.execute(sql)
        conn.commit()
        print("Books table created successfully")

    @classmethod
    def drop_table(cls):
        sql = "DROP TABLE IF EXISTS Books;"
        cursor.execute(sql)
        conn.commit()
        print("Books table dropped successfully")

    def save(self):#rows
        sql = """
            INSERT INTO Books (title, author, isbn)
            VALUES (?, ?, ?)
        """
        cursor.execute(sql, (self.title, self.author, self.isbn))
        conn.commit()
        self.id = cursor.lastrowid

    @classmethod
    def create(cls, title, author, isbn):
        book = cls(None, title, author, isbn)
        book.save()
        return book

    @classmethod
    def find_by_id(cls, id):
        sql = "SELECT * FROM Books WHERE id = ?"
        cursor.execute(sql, (id,))
        row = cursor.fetchone()
        return cls(*row) if row else None

    @classmethod
    def find_by_title(cls, title):
        sql = "SELECT * FROM Books WHERE title = ?"
        cursor.execute(sql, (title,))
        rows = cursor.fetchall()
        books = [cls(*row) for row in rows]
        return books

    @classmethod
    def find_by_isbn(cls, isbn):
        sql = "SELECT * FROM Books WHERE isbn = ?"
        cursor.execute(sql, (isbn,))
        row = cursor.fetchone()
        return cls(*row) if row else None

    @classmethod
    def select(cls):
        sql = "SELECT * FROM Books"
        cursor.execute(sql)
        rows = cursor.fetchall()
        books = [cls(*row) for row in rows]
        return books

    def delete(self):
        sql = "DELETE FROM Books WHERE id = ?"
        cursor.execute(sql, (self.id,))
        conn.commit()

    def update(self, title=None, author=None, isbn=None):
        self.title = title 
        self.author = author 
        self.isbn = isbn 
        sql = """
            UPDATE Books
            SET title = ?, author = ?, isbn = ?
            WHERE id = ?
        """
        cursor.execute(sql, (self.title, self.author, self.isbn, self.id))
        conn.commit()
