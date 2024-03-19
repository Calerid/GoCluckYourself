import sqlite3
import time

# Create database connection
def create_connection(db_file):
    connect = None
    try:
        connect = sqlite3.connect(db_file)
        print("SQLite connection established")
        time.sleep(2)
    except sqlite3.Error as sqliteError:
        print(sqliteError)
    return connect        

# Initializes all tables in the database.
# Fails if the tables cannot be initialized.
def create_tables(connect):
    try:
        cursor = connect.cursor()

        #Customers table
        cursor.execute('''CREATE TABLE IF NOT EXISTS customer
                       (customer_id INTEGER PRIMARY KEY,
                       name TEXT NOT NULL,
                       phone INTEGER,
                       business TEXT NULL, 
                       notes TEXT NULL)''')
        
        print("Customer table creation complete")
        time.sleep(2)
        
        # Sales table
        cursor.execute('''CREATE TABLE IF NOT EXISTS sales
                       (transaction_id INTEGER PRIMARY KEY,
                       customer_id INTEGER,
                       date TEXT,
                       amount REAL,
                       eggs_sold INTEGER,
                       FOREIGN KEY(customer_id) REFERENCES customer(customer_id))''')
        
        print("Sales table creation complete")
        time.sleep(2)
        
        #Chicken table
        cursor.execute('''CREATE TABLE IF NOT EXISTS chickens
                       (chicken_id INTEGER PRIMARY KEY,
                       name TEXT,
                       breed TEXT,
                       birth TEXT,
                       cost REAL,
                       death TEXT NULL,
                       status TEXT,
                       sale_price REAL)''')
        
        print("Chicken table creation complete")
        time.sleep(2)

        connect.commit()
        print("Tables initialized successfully")
        time.sleep(2)
    except sqlite3.Error as sqLiteTableFailure:
        print(sqLiteTableFailure)

class DatabaseFunctions:

    def create_new_entry(table, column, payload):
        conn = sqlite3.connect('go_cluck_yourself.db')

    def get_last_id(table, column):
        conn = sqlite3.connect('go_cluck_yourself.db')
        cursor = conn.cursor()
        query = f"SELECT MAX {column} FROM {table}"
        
        cursor.execute(query)
        last_id = cursor.fetchone()[0]

        cursor.close()
        conn.close()

        return last_id

        
        



