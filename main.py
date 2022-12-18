import pathlib
import tkinter as tk
import random
import tkinter.font as TkFont
from tkinter import *
import os
import time

time.sleep(10)

if os.environ.get('DISPLAY','') == '':
    print('no display found. Using :0.0')
    os.environ.__setitem__('DISPLAY', ':0.0')

file = pathlib.Path("./messages.txt")
lines = file.open().read().split('\n')

message = lines[random.randrange(0,len(lines))]

r = lambda: random.randint(0,255)
color = '#%02X%02X%02X' % (r(),r(),r())

root = tk.Tk()
root.configure(bg="white")
root.title("Message of the Day")
#root.geometry("480x320")
root.attributes("-fullscreen",True)
screen_width = root.winfo_screenwidth()
screen_height = root.winfo_screenheight()

# canvas = tk.Canvas(root, height=screen_height,width=screen_width,bg="black")

# Create label
l = Label(root, text = message,bg="black",fg=color, height=480,width=320)
l.config(font =("Courier", 40))
l.pack()

# frame = tk.Frame(root,bg="white")
# frame.place(relwidth=0.8,relheight=0.8)

root.mainloop()