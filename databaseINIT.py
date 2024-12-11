import sqlite3

def init_db():
    conn = sqlite3.connect('recommendations.db')
    cursor = conn.cursor()
    cursor.execute('''
        CREATE TABLE IF NOT EXISTS recommendations (
            id INTEGER PRIMARY KEY AUTOINCREMENT,
            data TEXT NOT NULL,
            audience TEXT NOT NULL
        )
    ''')
    conn.commit()
    conn.close()

def populate_db():
    conn = sqlite3.connect('recommendations.db')
    cursor = conn.cursor()
    sample_data = [

    ]
    cursor.executemany('INSERT INTO recommendations (data, audience) VALUES (?, ?)', sample_data)
    conn.commit()
    conn.close()