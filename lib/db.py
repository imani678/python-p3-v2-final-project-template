# db.py

import sqlite3

conn = sqlite3.connect('library.db')
cursor = conn.cursor()
