import sqlite3

# Create database connection
def create_connection(db_file):
    conn = None
    try:
        create_connection = sqlite3.connect(db_file)
        print("SQLite connection established")
    except sqlite3.Error as sqliteError:
        print(sqliteError)
    return create_connection         

# Initializes all tables in the database.
# Fails if the tables cannot be initialized.
def create_tables(db_connection):
    try:
        cursor = create_connection()
        
        #sales table
        cursor.execute('''CREATE TABLE IF NOT EXISTS sales
                       transaction_id INTEGER PRIMARY KEY,
                       FOREIGN KEY(customer) REFERENCES customer(customer_id))
                       date TEXT,
                       amount REAL,
                       eggs_sold INTEGER,
                       ''')
        
        print("Sales table creation complete")
        
        #Customers table
        cursor.execute('''CREATE TABLE IF NOT EXISTS customer
                       customer_id INTEGER PRIMARY KEY,
                       name TEXT,
                       phone INTEGER,
                       notes TEXT,
                       ''')
        
        print("Customer table creation complete")
        
        #Chicken table
        cursor.execute('''CREATE TABLE IF NOT EXISTS chickens
                       chicken_id INTEGER PRIMARY KEY,
                       name TEXT,
                       breed TEXT,
                       birth TEXT,
                       cost REAL,
                       ''')
        print("Chicken table creation complete")

        db_connection.commit()
        print("Tables initialized successfully")
    except sqlite3.Error as sqLiteTableFailure:
        print(sqLiteTableFailure)

