from database import create_connection, create_tables

def main():
    database = "go_cluck_yourself.db"
    connection = create_connection(database)
    if connection is not None:
        # Establishes tables
        create_tables(connection)
        connection.close()

        print("database connection completed")
        
    else:
        print("An error occured during DB creation. Connection not established or error in table creation.")