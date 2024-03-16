import sqlite3

# Create database connection
def create_connection(db_file)
    conn = None
    try:
        db_connection = sqlite3.connect(db_file)
        print("SQLite connection established")
    except sqlite3.Error as sqliteError:
        print(sqliteError)
    return db_connection         

# Initializes all tables in the database.
# Fails if the tables cannot be initialized.
def create_tables(db_connection):
    try:
        cursor = db_connection()
        
        #sales table
        cursor.execute('''CREATE TABLE IF NOT EXISTS sales
                       sale INTEGER PRIMARY KEY,
                       date TEXT,
                       amount REAL,
                       eggs_sold INTEGER,
                       FOREIGN KEY(customer) REFERENCES customer(customer_id))
                       ''')
        
        #Customers table
        cursor.execute('''CREATE TABLE IF NOT EXISTS customer
                       customer_id INTEGER PRIMARY KEY,
                       name TEXT,
                       phone INTEGER,
                       notes TEXT,
                       
                       ''')
        
        #Chicken table
        cursor.execute('''CREATE TABLE IF NOT EXISTS chickens
                       id INTEGER PRIMARY KEY,
                       name TEXT,
                       breed TEXT,
                       birth TEXT,
                       cost REAL,
                       ''')
        
        cursor.execute(''''CREATE TABLE IF NOT EXISTS customer
                       ''')

        db_connection.commit()
        print("Tables initialized successfully")
    except sqlite3.Error as sqLiteTableFailure:
        print(sqLiteTableFailure)

