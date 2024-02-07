"""
A menu - you need to add the database and fill in the functions. 
"""
import sqlite3

db = 'chainsaw_records.sqlite'

# Create table
create_table_sql = """
--sql
CREATE TABLE IF NOT EXISTS records 
(name text, country text, "number of catches" int)
;
"""
sample_data_sql = """
--sql
INSERT INTO records VALUES
('Janne Mustonen', 'Finland', 98),
('Ian Stewart', 'Canada', 94),
('Aaron Gregg', 'Canada', 88),
('Chad Taylor', 'USA', 78)
;
"""
with sqlite3.connect(db) as conn:
    conn.execute(create_table_sql)
    conn.execute(sample_data_sql)
conn.close()


def main():
    menu_text = """
    1. Display all records
    2. Search by name
    3. Add new record
    4. Edit existing record
    5. Delete record 
    6. Quit
    """

    while True:
        print(menu_text)
        choice = input('Enter your choice: ')
        if choice == '1':
            display_all_records()
        elif choice == '2':
            search_by_name()
        elif choice == '3':
            add_new_record()
        elif choice == '4':
            edit_existing_record()
        elif choice == '5':
            delete_record()
        elif choice == '6':
            break
        else:
            print('Not a valid selection, please try again')


def display_all_records():
    conn = sqlite3.connect(db)
    results = conn.execute('SELECT * FROM records')
    print("\nCurrent records:")
    for row in results:
        print(row)

def search_by_name():
    name_request =  input("Please enter a full name to search for: ")
    conn = sqlite3.connect(db)
    results = conn.execute('SELECT * FROM records WHERE name like ?', (name_request,)) # comma required for tuple
    first_row = results.fetchone()
    if first_row:
        print(first_row)
    else:
        print(f'{name_request} not found')


def add_new_record():
    new_name = input("Name: ") 
    new_country = input("Country: ")
    new_number_of_catches = int(input("Number of catches: "))
    with sqlite3.connect(db) as conn:
        conn.execute(f'INSERT INTO records VALUES (?, ?, ?)', (new_name, new_country, new_number_of_catches))
    conn.close()
    print('todo add new record. What if user wants to add a record that already exists?')


def edit_existing_record():
    user_input_name = input("Which entry would you like to edit? Give me a name and you can edit the number of catches")
    user_input_number = input("What is the updated catch number?")
    edit_query='UPDATE records SET "number of catches" = ? WHERE name = ?'
    with sqlite3.connect(db) as conn:
        conn.execute(edit_query, (user_input_number, user_input_name))
    conn.close()

def delete_record(): 
    user_input = input("What entry would you like to delete (based on name)?")
    delete_query='DELETE FROM records WHERE name = ?'
    with sqlite3.connect(db) as conn:
        conn.execute(delete_query, (user_input,))
    conn.close()


if __name__ == '__main__':
    main()