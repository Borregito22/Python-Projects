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
s1 = StringVar()
s2 = StringVar()

# Set buttons and Entry boxes and grid them to window
b1 = Button(win, text="Browse...", command=lambda: get_directory())
b1.grid(row=0, column=0, padx=(10,0), pady=(15,0), sticky=EW)
b2 = Button(win, text="Browse...", command=lambda: get_directory())
b2.grid(row=1, column=0, padx=(10,0), pady=(15,0), sticky=EW)
b3 = Button(win, text="Check for files...", height=2, command=lambda: last_mod_time(fname))
b3.grid(row=2, column=0, padx=(10,0), pady=(15,0))
b4 = Button(win, text="Close Program", height=2)
b4.grid(row=2, column=3, padx=(10,0), pady=(15,0), sticky=E)
e1 = Entry(width=55, text="", textvariable=s1)
e1.grid(row=0, column=1, columnspan=3, padx=(15,0), pady=(10,0), sticky=EW)
e2 = Entry(width=55, text="", textvariable=s2)
e2.grid(row=1, column=1, columnspan=3, padx=(15,0), pady=(10,0), sticky=EW)

# selecting a directory
def get_directory():
    b1 = filedialog.askdirectory(title = "Select Directory")
    s1.set(b1)
    b2 = filedialog.askdirectory(title = "Select Directory")
    s2.set(b2)
    
# time() works with seconds, so we need to get the seconds in 24 hours
Seconds_in_day = 24 * 60 * 60

# Set where the source of the files are
source = '{}'.format(s1.get())

# Set the destination path to FolderB
destination = '{}'.format(s2.get())

# Sets the current time as a floating point number
now = time.time()
# Removes 24 hours from current time
before = now - Seconds_in_day

# Sets the time of the last time the file was modified/created
def last_mod_time(fname):
    return os.path.getmtime(fname)

# We're stating to copy the files represented by 'fname' to their new destination
for fname in os.listdir(source):
    source_fname = os.path.join(source, fname)
    if last_mod_time(source_fname) > before:
        destination_fname = os.path.join(destination, fname)
        if fname.endswith('.txt'): # Only copy files that end with '.txt'
            shutil.copy(source_fname, destination_fname)
