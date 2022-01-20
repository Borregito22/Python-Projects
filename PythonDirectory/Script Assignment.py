import os
import time

fPath = 'C:\\Users\\niels\\Documents\\PythonDirectory'

# Req 2: listdir() to iterate through all files within directory
dir_list = os.listdir(fPath)

# Req 3: path.join() to concatenate the file name to its file path
for root, dirs, files in os.walk(os.path.abspath("../PythonDirectory")):
    for file in files:
        print(os.path.join(root, file))

# Req 4: getmtime() to find latest date that each text file has been created or modified
m_time = os.path.getmtime(fPath)
print(m_time)

# Req 5: 
data = []
for names in dir_list:
    if names.endswith(".txt"):
        data.append(names)
print(data)
