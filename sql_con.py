import sqlite3

def get_db_conection():
    conn = sqlite3.connect('info.db')
    conn.row_factory = sqlite3.Row
    return conn