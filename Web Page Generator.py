import webbrowser
from tkinter import *
import os

# Creating the GUI
win = Tk()
win.title("Web Page Generator")
win.geometry("280x50")
b1 = Button(win, text="Click here to confirm body", command=lambda:Body())
b1.pack(side=BOTTOM)
e1 = Entry(win, text="")
e1.pack(side=TOP)

# All code for writing content to the HTML should be in one function
def Body():
    # .get will grab the text curerntly in Entry field
    text = e1.get()
    # HTML code
    message = """
    <html>
        <body>
            <h1>
                {}
            </h1>
        </body>
    </html>
    """.format(text)
    # Opens/creates new file
    f = open('webpagegen.html','w')
    # Writes code into file
    f.write(message)
    f.close()

# Opens a new tab on current browser
filename = 'file:///'+os.getcwd()+'/' + 'webpagegen.html'
webbrowser.open_new_tab(filename)

win.mainloop()
