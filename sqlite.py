import sqlite3

# Connect to SQLite database (creates it if it doesn't exist)
connection = sqlite3.connect("student.db")

# Create a cursor object to execute SQL commands
cursor = connection.cursor()

# Create the STUDENT table
table_info = """
CREATE TABLE IF NOT EXISTS STUDENT (
    NAME VARCHAR(25),
    CLASS VARCHAR(25),
    SECTION VARCHAR(25),
    MARKS INT
)
"""
cursor.execute(table_info)

# Insert some records
cursor.execute("""INSERT INTO STUDENT VALUES ('Krish', 'Data Science', 'A', 90)""")
cursor.execute("""INSERT INTO STUDENT VALUES ('John', 'Data Science', 'B', 100)""")
cursor.execute("""INSERT INTO STUDENT VALUES ('Mukesh', 'Data Science', 'A', 86)""")
cursor.execute("""INSERT INTO STUDENT VALUES ('Jacob', 'DEVOPS', 'A', 50)""")
cursor.execute("""INSERT INTO STUDENT VALUES ('Dipesh', 'DEVOPS', 'A', 35)""")

# Display all the records
print("The inserted records are:")
data = cursor.execute("SELECT * FROM STUDENT")
for row in data:
    print(row)

# Commit changes and close connection
connection.commit()
connection.close()
