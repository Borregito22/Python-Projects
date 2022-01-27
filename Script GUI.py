from tkinter import *

win = Tk()
win.minsize(475, 170)
win.maxsize(475, 170)
win.title("Check files")

b1 = Button(win, text="Browse...")
b1.grid(row=0, column=0, padx=(10,0), pady=(15,0), sticky=EW)
b2 = Button(win, text="Browse...")
b2.grid(row=1, column=0, padx=(10,0), pady=(15,0), sticky=EW)
b3 = Button(win, text="Check for files...", height=2)
b3.grid(row=2, column=0, padx=(10,0), pady=(15,0))
b4 = Button(win, text="Close Program", height=2)
b4.grid(row=2, column=3, padx=(10,0), pady=(15,0), sticky=E)
e1 = Entry(text="")
e1.grid(row=0, column=1, columnspan=3, padx=(15,0), pady=(10,0), sticky=EW)
e2 = Entry(text="")
e2.grid(row=1, column=1, columnspan=3, padx=(15,0), pady=(10,0), sticky=EW)

# center window to user's screen
def center_window(w, h): # pass in the w and h
        # get user's screen width and height
        screen_width = win.winfo_screenwidth()
        screen_height = win.winfo_screenheight()
        # calculate x and y coordinates to paint the app centered on the user's screen
        x = int((screen_width/2) - (w/2))
        y = int((screen_height/2) - (h/2))
        centerGeo = win.geometry("{}x{}+{}+{}".format(w, h, x, y))
        return centerGeo
center_window(475, 170)

