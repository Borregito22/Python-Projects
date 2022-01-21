import sqlite3

# Connect to database, if it doesn't exist, it will create one
# Conn holds the connection to the database
conn = sqlite3.connect('dBAssignment.db')

# With loop says "while there's a connection, do the following code"
with conn:
    cur = conn.cursor() # Cursor operates the dB when commands are given
    # SQL statements will be wrapped by execute command
    cur.execute("CREATE TABLE IF NOT EXISTS tbl_files(\
        ID INTEGER PRIMARY KEY AUTOINCREMENT, \
        col_File VARCHAR(30) \
        )")
    conn.commit()
conn.close()

conn = sqlite3.connect('dBAssignment.db')

# Tuple of files
fileList = ('information.docx', 'Hello.txt', 'myImage.png', 'myMovie.mpg', \
            'World.txt', 'data.pdf', 'myPhoto.jpg')

# loop through each object in the tuple to find the files that end in ".txt"
for x in fileList:
    if x.endswith(".txt"):
        with conn:
            cur = conn.cursor()
            # The value for each row will be one name out of the tuple therefore (x,)
            # will denote a one element tuple for each name ending with ".txt"
            cur.execute("INSERT INTO tbl_files (col_File) VALUES (?)", (x,))
            print(x)
conn.close()
