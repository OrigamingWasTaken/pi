import pathlib
import tkinter as tk
import random
import tkinter.font as font
from tkinter import *
import os
import time
from datetime import date
import json
import glob
from PIL import Image, ImageTk

if os.environ.get('DISPLAY','') == '':
    print('no display found. Using :0.0')
    os.environ.__setitem__('DISPLAY', ':0.0')

images = glob.glob("images/*")
image = Image.open(random.choice(images))

# Create a transparent overlay with the same size as the image
overlay = Image.new('RGBA', image.size, (255, 255, 255, 51))  # 51 is the transparency level (0-255)

# Paste the overlay onto the image
image.alpha_composite(overlay)

# Create a PhotoImage object from the image

file = pathlib.Path("./messages.txt")
lines = file.open().read().split('\n')

specialFile = pathlib.Path("./special.json")
dates = json.load(specialFile.open())

message = lines[random.randrange(0,len(lines))]

date = str(date.today())[5:]

try:
    message = dates[date]
except Exception:
    pass

def random_color():
        rand = lambda: random.randint(1, 200)
        return '#%02X%02X%02X' % (rand(), rand(), rand())

r = lambda: random.randint(0,255)
color = random_color()

root = tk.Tk()
root.configure(bg="white")
root.title("Message of the Day")
root.attributes("-fullscreen",True)
screen_width = root.winfo_screenwidth()
screen_height = root.winfo_screenheight()

Grid.columnconfigure(root, index=0, weight=1)
Grid.rowconfigure(root, 0, weight=1)

image = ImageTk.PhotoImage(image)

imageLabel = Label(image=image)
label = Label(root, text=message, bg="white", fg=color, wraplength=root.winfo_width())

# Position the image label and text label on top of each other using the place geometry manager
imageLabel.place(x=0, y=0, relwidth=1, relheight=1)
label.place(x=0, y=0, relwidth=1, relheight=1)

# Resize the image using the Image.resize method
image = image.resize((imageLabel.winfo_width(), imageLabel.winfo_height()))

# Update the image displayed by the image label
imageLabel.configure(image=image)

# Add the widgets to the root window using the grid geometry manager
label.grid(row=0,column=0,sticky="nsew")
imageLabel.grid(row=1,column=0,sticky="nsew")

def update_label_text(event):
    # Get the width and height of the window
    width = event.width
    height = event.height

    # Calculate the font size based on the width and height of the window
    font_size = int(min(width, height) / 10)

    # Update the font size of the label
    label.config(font=("Helvetica", font_size),wraplength=width)
 
root.bind("<Configure>", update_label_text)
root.mainloop()