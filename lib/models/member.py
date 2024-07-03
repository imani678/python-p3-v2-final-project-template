

from db import conn, cursor

class Member:
    def __init__(self, id, name, email):
        self.id = id
        self.name = name
        self.email = email

    def __repr__(self):
        return f"<Member {self.id} {self.name} {self.email}>"

    @classmethod
    def create_table(cls):
        sql = """
            CREATE TABLE IF NOT EXISTS Members (
                id INTEGER PRIMARY KEY AUTOINCREMENT,
                name TEXT NOT NULL,
                email TEXT NOT NULL UNIQUE
            )
        """
        cursor.execute(sql)
        conn.commit()
        print("Members table created successfully")

    @classmethod
    def drop_table(cls):
        sql = "DROP TABLE IF EXISTS Members;"
        cursor.execute(sql)
        conn.commit()
        print("Members table dropped successfully")

    def save(self):
        sql = """
            INSERT INTO Members (name, email)
            VALUES (?, ?)
        """
        cursor.execute(sql, (self.name, self.email))
        conn.commit()
        self.id = cursor.lastrowid

    @classmethod
    def create(cls, name, email):
        member = cls(None, name, email)
        member.save()
        return member

    @classmethod
    def find_by_id(cls, id):
        sql = "SELECT * FROM Members WHERE id = ?"
        cursor.execute(sql, (id,))
        row = cursor.fetchone()
        return cls(*row) if row else None

    @classmethod
    def find_by_name(cls, name):
        sql = "SELECT * FROM Members WHERE name = ?"
        cursor.execute(sql, (name,))
        rows = cursor.fetchall()
        members = [cls(*row) for row in rows]
        return members

    @classmethod
    def find_by_email(cls, email):
        sql = "SELECT * FROM Members WHERE email = ?"
        cursor.execute(sql, (email,))
        row = cursor.fetchone()
        return cls(*row) if row else None

    @classmethod
    def select(cls):
        sql = "SELECT * FROM Members"
        cursor.execute(sql)
        rows = cursor.fetchall()
        members = [cls(*row) for row in rows]
        return members

    def delete(self):
        sql = "DELETE FROM Members WHERE id = ?"
        cursor.execute(sql, (self.id,))
        conn.commit()

    def update(self, name=None, email=None):
        self.name = name or self.name
        self.email = email or self.email
        sql = """
            UPDATE Members
            SET name = ?, email = ?
            WHERE id = ?
        """
        cursor.execute(sql, (self.name, self.email, self.id))
        conn.commit()
