import os, datetime, random, json
import tkinter as tk
from tkinter import *

# Set Screen
if os.environ.get('DISPLAY','') == '':
    print('No display found. Using :0.0')
    os.environ.__setitem__('DISPLAY', ':0.0')

# Get the message
def getMessage():
    # Check if today is a special date
    today = str(datetime.date.today())[5:]
    dates = json.load(open("special.json","r"))
    if today in dates:
         return dates[today]

    messages = open("messages.txt","r").read().split("\n")
    
    # If file is empty then restore the backup
    if messages == ['']:
        with open("messages.txt","w+") as a:
            sourceContent = open("save/messages.txt","r").read()
            messages = sourceContent.split("\n")
            a.write(sourceContent)

    # Delete the line used for today's message so the messages can't repeat
    message = messages.pop(random.randrange(0, len(messages)))
    with open("messages.txt","w+") as f:
        for line in messages:
            f.write(line + "\n")
        f.close()
    return message

def getColor():
        # Returns a easily on-white readble color
        rand = lambda: random.randint(1, 200)
        return '#%02X%02X%02X' % (rand(), rand(), rand())

# Create the window
root = tk.Tk()
root.configure(bg="white")
root.title("Message of the Day")
root.attributes("-fullscreen",True)
screen_width = root.winfo_screenwidth()
screen_height = root.winfo_screenheight()

Grid.columnconfigure(root, index=0, weight=1)
Grid.rowconfigure(root, 0, weight=1)

label = Label(root, text=getMessage(), bg="white", fg=getColor(), wraplength=root.winfo_width())

label.place(x=0, y=0, relwidth=1, relheight=1)

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
 
root.bind("<Configure>", update_label_text)
root.mainloop()