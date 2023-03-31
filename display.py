from tkinter import *
import tkinter as tk
import os
import time
import random
import json
import datetime
from datetime import date
from PIL import Image, ImageTk

if os.environ.get('DISPLAY','') == '':
    print('no display found. Using :0.0')
    os.environ.__setitem__('DISPLAY', ':0.0')

#Get the special messages
with open("./special.json") as specialFile:
    dates = json.load(specialFile)

#Set the message
def getMessage():
    with open("./messages.txt","r+") as file:
        lines = file.readlines()
        if len(lines) == 0:
            with open("messages.txt","w+") as o_f:
                b_lines = open("messages_save.txt","r").readlines()
                o_f.writelines(b_lines)
                lines = b_lines
                o_f.close()
        message = lines[0]
    today = str(date.today())[5:]
    try:
        message = dates[today]
    except Exception:
        del lines[0]
        with open("./messages.txt","w+") as file:
            file.writelines(lines)
    return(message)


#Check if today is a special date, if yes then display the correct message

#Make a random color for the text, that isn't too bright so it can be read on a white bg
def random_color():
        rand = lambda: random.randint(1, 200)
        return '#%02X%02X%02X' % (rand(), rand(), rand())

print("Lets go!")

while True:
    root = tk.Tk()
    root.configure(bg="white")
    root.title("Message of the Day")
    root.attributes("-fullscreen",True)
    screen_width = root.winfo_screenwidth()
    screen_height = root.winfo_screenheight()

    Grid.columnconfigure(root, index=0, weight=1)
    Grid.rowconfigure(root, 0, weight=1)

    label = Label(root, text="Loading...", bg="white", fg=random_color(), wraplength=root.winfo_width())

    # Position the image label and text label on top of each other using the place geometry manager
    label.place(x=0, y=0, relwidth=1, relheight=1)

    # Resize the image using the Image.resize method

    # Update the image displayed by the image label

    # Add the widgets to the root window using the grid geometry manager
    label.grid(row=0,column=0,sticky="nsew")

    def update_label_text(event):
        # Get the width and height of the window
        width = event.width
        height = event.height

        # Calculate the font size based on the width and height of the window
        font_size = int(min(width, height) / 10)

        # Update the font size of the label
        label.config(font=("Helvetica", font_size),wraplength=width)

    def update_message():
        today = datetime.date.today()
        label.config(text=getMessage(),fg=random_color())

        tomorrow = today + datetime.timedelta(days=1)
        midnight = datetime.datetime.combine(tomorrow, datetime.time.min)
        #root.after(5000,update_message)
        root.after((midnight - datetime.datetime.now()).seconds * 1000, update_message)

    update_message()
    
    root.bind("<Configure>", update_label_text)
    root.mainloop()