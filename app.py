import time
import models
from blessed import Terminal
from database import create_connection, create_tables


def main():
    term = Terminal()
    app_name = term.bold("Go Cluck Yourself")
    title_print = term.underline(f"{app_name}\nAuthor: Michael Braley \nGithub: {term.link('https://github.com/Calerid', '@Calerid')}")
    with term.fullscreen(), term.cbreak():
        print(title_print)
        database = "go_cluck_yourself.db"
        connection = create_connection(database)
        if connection is not None:
            try:
                create_tables(connection)
                connection.close()
                print("Database tables initialized successfully")
                time.sleep(5)
                print(term.clear())
            except Exception as e:
                print(f"An error occurred during table creation: {e}")
        else:
            print("An error occurred during database connection establishment.")    
    def selection_loop(connection):
        while True:
            print(term.clear())
            print(title_print)
            print("1. Chicken Tools")
            print("2. Customer Tools")
            print("3. Sales Manager")        
            with term.cbreak():
                val = ''
                val = term.inkey()
                if val == "1":
                    create_chicken()
                elif val == "":
                    selection_loop()

    def create_chicken():
        val = ''
        val = term.inkey()
        print(term.clear())
        print(title_print)
        print("1. Create a chicken")
        print("2. Update existing chicken")
        with term.cbreak():
            val = ''
            val = term.inkey()
            if val == "1":
                print("creating chicken")
            else:
                create_chicken()    

    selection_loop(connection)


if __name__ == "__main__":
    main()