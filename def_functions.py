import string
import secrets
import sqlite3

def gen_pass(): # Generate a random password by choosing from string of symbols, numbers, and upper and lower case letters.
    symbols = """!"#$%&'()*+,-./:;<=>?@[\]^_`{|}~""" # Add or remove symbols on this line.
    password = ""
    for _ in range(3):
        password += secrets.choice(string.ascii_lowercase)
        password += secrets.choice(string.ascii_uppercase)
        password += secrets.choice(string.digits)
        password += secrets.choice(symbols)
    return password

def connect(): # Connect to the database called passwords.db or create it if it doesn't exist and create a table called passwords inside it with the columns app, url, user, and psswd.
    conn = sqlite3.connect("passwords.db")
    cursor = conn.cursor()
    cursor.execute('''
    CREATE TABLE IF NOT EXISTS passwords (
        app TEXT,
        url TEXT,
        user TEXT,
        psswd TEXT
    )
    ''')
    conn.commit()
    conn.close()


def search(term): # Conduct a fuzzy search in the passwords.db database with the term arg and return the results in a list.
    database = "passwords.db"
    conn = sqlite3.connect(database)
    cursor = conn.cursor()
    search_term = "%" + term + "%"
    fuzzy_search = '''SELECT * FROM passwords WHERE app LIKE ?'''
    cursor.execute(fuzzy_search, (search_term,))
    fuzzy_search_results = cursor.fetchall()
    results = []
    for result in fuzzy_search_results:
        app, url, user, psswd = result
        results.append((app, url, user, psswd))
    conn.close()
    return results

def insert(app, url, user, psswd): # Insert the contents of the args provided into the passwords.db database.
    database = "passwords.db"
    conn = sqlite3.connect(database)
    cursor = conn.cursor()
    insert_query = '''INSERT INTO passwords (app, url, user, psswd) VALUES (?, ?, ?, ?)'''
    data_tuple = (app, url, user, psswd)
    cursor.execute(insert_query, data_tuple)
    conn.commit()
    conn.close()

def delete(app_name): # Delete the database entry by the name provided in the app_name arg.
    database = "passwords.db"
    conn = sqlite3.connect(database)
    cursor = conn.cursor()

    delete_query = '''DELETE FROM passwords WHERE app = ?'''
    cursor.execute(delete_query, (app_name,))
    
    conn.commit()
    conn.close()