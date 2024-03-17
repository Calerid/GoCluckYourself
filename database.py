import sqlite3

# Create database connection
def create_connection(db_file):
    connect = None
    try:
        connect = sqlite3.connect(db_file)
        print("SQLite connection established")
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
        
        # Sales table
        cursor.execute('''CREATE TABLE IF NOT EXISTS sales
                       (transaction_id INTEGER PRIMARY KEY,
                       customer_id INTEGER,
                       date TEXT,
                       amount REAL,
                       eggs_sold INTEGER,
                       FOREIGN KEY(customer_id) REFERENCES customer(customer_id))''')
        
        print("Sales table creation complete")
        
        #Chicken table
        cursor.execute('''CREATE TABLE IF NOT EXISTS chickens
                       (chicken_id INTEGER PRIMARY KEY,
                       name TEXT,
                       breed TEXT,
                       birth TEXT,
                       cost REAL)''')
        
        print("Chicken table creation complete")

        connect.commit()
        print("Tables initialized successfully")
    except sqlite3.Error as sqLiteTableFailure:
        print(sqLiteTableFailure)

