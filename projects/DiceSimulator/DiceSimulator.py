import tkinter
from PIL import Image,ImageTk
import random

root=tkinter.Tk()
root.geometry('200x200')
root.title('DICE SIMULATION BY SHIVANI CHITIKESI')

# Adding label into the frame
BlankLine = tkinter.Label(root, text="")
BlankLine.pack()# Adding label into the frame
BlankLine = tkinter.Label(root, text="")
BlankLine.pack()

# adding label with different font and formatting
HeadingLabel = tkinter.Label(root, text="Hello from DataFlair!",
   fg = "light green",
     bg = "dark green",
     font = "Helvetica 16 bold italic")
HeadingLabel.pack()
