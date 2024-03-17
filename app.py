from database import create_connection, create_tables

def main():
    database = "go_cluck_yourself.db"
    connection = create_connection(database)
    if connection is not None:
        try:
            create_tables(connection)
            connection.close()
            print("Database tables initialized successfully")
        except Exception as e:
            print(f"An error occurred during table creation: {e}")
    else:
        print("An error occurred during database connection establishment.")

if __name__ == "__main__":
    main()