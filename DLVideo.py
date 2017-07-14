# requirement installation "pip install pafy"
from tkinter import *
from tkinter.filedialog import * #to open and find files
from PIL import Image, ImageTk

def callback():
    print ("called the callback!")

root = Tk()

#canvas
im = PhotoImage(file='bg.png')
# back_ground = ImageTk.PhotoImage(im)
canvas = Canvas(root,width=550, height=400)
canvas.create_image(250, 250, anchor='center', image=im)
canvas.pack()

# save file:
def find_direction():
    location_file = askopenfilename(title="Save your directory",filetypes=[('video files','.mp4','.avi'),('all files','.*')])


# create a menu
menu = Menu(root)
root.config(menu=menu)

filemenu = Menu(menu)
menu.add_cascade(label="File", menu=filemenu)
filemenu.add_command(label="New", command=find_direction)
filemenu.add_command(label="Open...", command=callback)
filemenu.add_separator()
filemenu.add_command(label="Exit", command=callback)

helpmenu = Menu(menu)
menu.add_cascade(label="Help", menu=helpmenu)
helpmenu.add_command(label="About...", command=callback)

mainloop()