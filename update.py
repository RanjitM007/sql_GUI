import sqlite3

sqliteConnection = sqlite3.connect('__iamri__.db')
cursor = sqliteConnection.cursor()
cursor.execute('''CREATE TABLE IF NOT EXISTS new_employee ( id INTEGER PRIMARY KEY, name TEXT NOT NULL, photo BLOB NOT NULL, resume BLOB NOT NULL);''')

cursor.close()
sqliteConnection.commit()
sqliteConnection.close()

def convertToBinaryData(filename):
    # Convert digital data to binary format
    with open(filename, 'rb') as file:
        blobData = file.read()
    return blobData

def insertBLOB(empId, name, photo, resumeFile):
    try:
        sqliteConnection = sqlite3.connect('__iamri__.db')
        cursor = sqliteConnection.cursor()
        print("Connected to SQLite")
        sqlite_insert_blob_query = """ INSERT INTO new_employee
                                  (id, name, photo, resume) VALUES (?, ?, ?, ?)"""

        empPhoto = convertToBinaryData(photo)
        resume = convertToBinaryData(resumeFile)
        # Convert data into tuple format
        data_tuple = (empId, name, empPhoto, resume)
        cursor.execute(sqlite_insert_blob_query, data_tuple)
        sqliteConnection.commit()
        print("Image and file inserted successfully as a BLOB into a table")
        cursor.close()

    except sqlite3.Error as error:
        print("Failed to insert blob data into sqlite table", error)
    finally:
        if sqliteConnection:
            sqliteConnection.close()
            print("the sqlite connection is closed")

insertBLOB(1, "Library", "C:/Users/Ranjit M/Desktop/Google/fruits/fruits1.jpg", "C:/Users/Ranjit M/Desktop/base.txt")
insertBLOB(2, "pip", "C:/Users/Ranjit M/Desktop/Google/fruits/fruits36.jpg","C:/Users/Ranjit M/Desktop/talkingbot.txt")
