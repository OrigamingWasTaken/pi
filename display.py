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

    # Remove blank lines
    with open("messages.txt", "r") as file:
        lines = file.readlines()
        non_blank_lines = [line for line in lines if line.strip() != ""]
    with open("messages.txt", "w") as file:
        file.writelines(non_blank_lines)

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
def update_canvas_text(event):
    canvas.delete("text")  # Remove any existing text
    width = event.width
    height = event.height

    # Calculate the font size based on the canvas dimensions
    font_size = min(width, height) // len(message) * 7  # Adjust as needed

    # Get the message and color
    color = getColor()

    # Draw the text on the Canvas (upside down) and wrap it on multiple lines
    canvas.create_text(
        width / 2,
        height / 2,
        text=message,
        font=("Helvetica", font_size),
        fill=color,
        angle=180,  # Rotate the text by 180 degrees (upside down)
        anchor="center",  # Center the text
        width=width - 40,  # Adjust as needed for text wrapping
        justify="center",  # Center the text within the width
        tags="text"
    )

message = getMessage()
root = tk.Tk()
root.configure(bg="white")
root.title("Message of the Day")
root.attributes("-fullscreen", True)

canvas = Canvas(root, bg="white", highlightthickness=0)
canvas.pack(fill=tk.BOTH, expand=True)

root.bind("<Configure>", update_canvas_text)
root.mainloop()