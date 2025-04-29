

from db import conn, cursor

class Loan:
    def __init__(self, id, book_id, member_id, loan_date, return_date):
        self.id = id
        self.book_id = book_id
        self.member_id = member_id
        self.loan_date = loan_date
        self.return_date = return_date

    def __repr__(self):
        return f"<Loan {self.id} Book ID: {self.book_id} Member ID: {self.member_id} Loan Date: {self.loan_date} Return Date: {self.return_date}>"

    @classmethod
    def create_table(cls):
        sql = """
            CREATE TABLE IF NOT EXISTS Loans (
                id INTEGER PRIMARY KEY AUTOINCREMENT,
                book_id INTEGER,
                member_id INTEGER,
                loan_date TEXT,
                return_date TEXT,
                FOREIGN KEY (book_id) REFERENCES Books (id),
                FOREIGN KEY (member_id) REFERENCES Members (id)
            )
        """
        cursor.execute(sql)
        conn.commit()
        print("Loans table created successfully")

    @classmethod
    def drop_table(cls):
        sql = "DROP TABLE IF EXISTS Loans;"
        cursor.execute(sql)
        conn.commit()
        print("Loans table dropped successfully")

    def save(self):
        sql = """
            INSERT INTO Loans (book_id, member_id, loan_date, return_date)
            VALUES (?, ?, ?, ?)
        """
        cursor.execute(sql, (self.book_id, self.member_id, self.loan_date, self.return_date))
        conn.commit()
        self.id = cursor.lastrowid

    @classmethod
    def create(cls, book_id, member_id, loan_date, return_date):
        loan = cls(None, book_id, member_id, loan_date, return_date)
        loan.save()
        return loan

    @classmethod
    def find_by_id(cls, id):
        sql = "SELECT * FROM Loans WHERE id = ?"
        cursor.execute(sql, (id,))
        row = cursor.fetchone()
        return cls(*row) if row else None

    @classmethod
    def select(cls):
        sql = "SELECT * FROM Loans"
        cursor.execute(sql)
        rows = cursor.fetchall()
        loans = [cls(*row) for row in rows]
        return loans

    def delete(self):
        sql = "DELETE FROM Loans WHERE id = ?"
        cursor.execute(sql, (self.id,))
        conn.commit()

    def update(self, book_id=None, member_id=None, loan_date=None, return_date=None):
        self.book_id = book_id or self.book_id
        self.member_id = member_id or self.member_id
        self.loan_date = loan_date or self.loan_date
        self.return_date = return_date or self.return_date
        sql = """
            UPDATE Loans
            SET book_id = ?, member_id = ?, loan_date = ?, return_date = ?
            WHERE id = ?
        """
        cursor.execute(sql, (self.book_id, self.member_id, self.loan_date, self.return_date, self.id))
        conn.commit()
