import shutil
import os
import time
from tkinter import *
from tkinter import filedialog

win = Tk()
win.minsize(475, 170)
win.maxsize(475, 170)
win.title("Check files")

# use tkinter.StringVar to print directory to e1/e2 after button click on b1
# must be set before e1/e2 can reference it
folderPathStart = StringVar()
folderPathEnd = StringVar()

# Set buttons and Entry boxes and grid them to window
b1 = Button(win, text="Browse...", command=lambda: start_directory())
b1.grid(row=0, column=0, padx=(10,0), pady=(15,0), sticky=EW)

b2 = Button(win, text="Browse...", command=lambda: end_directory())
b2.grid(row=1, column=0, padx=(10,0), pady=(15,0), sticky=EW)

b3 = Button(win, text="Check for files...", height=2, command=lambda: moveFiles())
b3.grid(row=2, column=0, padx=(10,0), pady=(15,0))

b4 = Button(win, text="Close Program", height=2)
b4.grid(row=2, column=3, padx=(10,0), pady=(15,0), sticky=E)

e1 = Entry(width=55, text=folderPathStart)
e1.grid(row=0, column=1, columnspan=3, padx=(15,0), pady=(10,0), sticky=EW)

e2 = Entry(width=55, text=folderPathEnd)
e2.grid(row=1, column=1, columnspan=3, padx=(15,0), pady=(10,0), sticky=EW)

# selecting a start and end directories
def start_directory():
    b1 = filedialog.askdirectory(title = "Select Directory")
    folderPathStart.set(b1)

def end_directory():
    b2 = filedialog.askdirectory(title = "Select Directory")
    folderPathEnd.set(b2)
    
# time() works with seconds, so we need to get the seconds in 24 hours
Seconds_in_day = 24 * 60 * 60

# Sets the current time as a floating point number
now = time.time()

# Removes 24 hours from current time
before = now - Seconds_in_day

# Gets the time of the last time the file was modified/created
def last_mod_time(i):
    return os.path.getmtime(i)

# Create a function for the file transfer
def moveFiles():
    source = folderPathStart.get()
    destination = folderPathEnd.get()
    source_files = os.listdir(source)
    
    for i in source_files:
        file_path = os.path.join(source, i)

        if last_mod_time(file_path) > before:
            shutil.move(source + '/' + i, destination)
            print (i + " File transfer successful!")
        else:
            print("No recent updates to files.")
