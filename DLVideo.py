# requirement installation "pip install pafy"
from tkinter import *
from tkinter.filedialog import * #to open and find files
from PIL import Image, ImageTk

class App:
    def __init__(self):
        root = Tk()
        root.title("Download Youtube")
        
        #canvas
        # im = PhotoImage(file='bg.png')
        # canvas = Canvas(root,width=550, height=400)
        # canvas.create_image(250, 250, anchor='center', image=im)
        # canvas.pack()

        # create a menu
        menu = Menu(root)
        root.config(menu=menu)

        filemenu = Menu(menu)
        menu.add_cascade(label="File", menu=filemenu)
        filemenu.add_command(label="New", command=self.find_direction)
        filemenu.add_command(label="Open...", command=self.find_direction)
        filemenu.add_separator()
        filemenu.add_command(label="Exit", command=exit)

        helpmenu = Menu(menu)
        menu.add_cascade(label="Help", menu=helpmenu)
        helpmenu.add_command(label="About...", command=self.find_direction)

        # Entry and label
        # fields = "Link Video", "Save"
        # ents = self.makeform(root, fields)
        url_label = Label(root, width=15, text="Link Video", bg="blue").grid(row=0,column=0)
        url = Entry(root).grid(row=0,column=1,padx=15,pady=15,ipadx=50,ipady=10,sticky="e")

        save_local_label = Label(root, width=15, text="Save Location", bg="blue").grid(row=1,column=0)
        save_local = Entry(root).grid(row=1,column=1,padx=15,pady=15,ipadx=50,ipady=10,sticky="e")
        
        # button
        b1 = Button(root, text="Download").grid(row=2,column=1,padx=15,sticky="w")
        # b1.pack(side=LEFT, padx=5, pady=5)

        b2 = Button(root, text='Quit', command=root.quit).grid(row=2,column=1,padx=15,sticky="e")
        # b2.pack(side=LEFT, padx=5, pady=5)

        b3 = Button(root, text='Here').grid(row=1, column=3)
        # b3.grid(row=1, column=3)
        # b3.pack(side=LEFT, padx=5, pady=5)
        # b3.place(relx=1, x=-2, y=10, anchor=NE)

        b4 = Button(root, text='...', bg="white")
        # b4.pack(side=LEFT, padx=5, pady=5)
        # b4.place(relx=1, x=-2, y=2, anchor=NE)

        # # label1 = Label(root, text='Link Video').grid(row=2, column=2)
        # # label2 = Label(root, text='Save').grid(row=4, column=2)

        # # entry1 = Entry(root).grid(row=2, column=3)
        # # entry2 = Entry(root).grid(row=4, column=3)

        mainloop()


    # save file:
    def find_direction(self):
        location_file = askopenfilename(title="Save your directory",filetypes=[('video files','.mp4','.avi'),('all files','.*')])
    
    def makeform(self, root, fields):
        entries = []
        for field in fields:
            row = Frame(root)
            lab = Label(row, width=15, text=field, anchor='w')
            ent = Entry(row)
            row.pack(side=TOP, fill=X, padx=5, pady=5)
            lab.pack(side=LEFT)
            ent.pack(side=RIGHT, expand=YES, fill=X)
            entries.append((field, ent))
        return entries

if __name__ == '__main__':
    App()
    