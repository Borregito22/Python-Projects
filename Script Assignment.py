# Req 1: Use Python 3 and OS module
import os
import time
import glob

fPath = 'C:\\Users\\niels\\Documents\\PythonDirectory'

# Req 2: listdir() to iterate through all files within directory
dir_list = os.listdir(fPath)
print(dir_list)

# Req 3: path.join() to concatenate the file name to its file path
for root, dirs, files in os.walk(os.path.abspath("../PythonDirectory")):
    for file in files:
        print(os.path.join(root, file))

# Req 4: getmtime() to find latest date that each text file has been created or modified
for file in dir_list:
    mTime = os.path.getmtime("../PythonDirectory/" + file)
    print(mTime)

# Req 5: Print each file ending with ".txt" and its corresponding mtime
for file in os.listdir(fPath):
    if file.endswith(".txt"):
        time_mod = os.path.getmtime(file)
        print(os.path.join(fPath, file))
        print(time_mod)
