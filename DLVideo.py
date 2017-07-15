from tkinter import *
from tkinter.filedialog import * #to open and find files
import pafy
import os

class App:
    def __init__(self):
        self.root = Tk()
        self.root.title("Download Youtube")
        
        #canvas
        # im = PhotoImage(file='bg.png')
        # canvas = Canvas(root,width=550, height=400)
        # canvas.create_image(250, 250, anchor='center', image=im)
        # canvas.pack()

        # create a menu
        self.menu = Menu(self.root)
        self.root.config(menu=self.menu)

        self.filemenu = Menu(self.menu)
        self.menu.add_cascade(label="File", menu=self.filemenu)
        self.filemenu.add_command(label="New")
        self.filemenu.add_command(label="Open...")
        self.filemenu.add_separator()
        self.filemenu.add_command(label="Exit", command=exit)

        self.helpmenu = Menu(self.menu)
        self.menu.add_cascade(label="Help", menu=self.helpmenu)
        self.helpmenu.add_command(label="About...")
        
        # button
        self.b1 = Button(self.root, text="Download", command=self.download)
        self.b1.grid(row=3,column=1,padx=15,sticky="w")
    
        self.b2 = Button(self.root, text='Quit', command=self.root.quit)
        self.b2.grid(row=3,column=1,padx=15,sticky="e")
        
        self.b3 = Button(self.root, text='...', bg="white", command=self.get_value_from_button)
        self.b3.grid(row=2, column=3)

        self.b4 = Button(self.root, text='...', command=lambda:self.url.delete(0, END))
        self.b4.grid(row=0, column=3)

        # Entry and label
        url_label = Label(self.root, width=15, text="Link Video", bg="blue").grid(row=0,column=0)
        self.url = Entry(self.root)
        self.url.grid(row=0,column=1,padx=15,pady=15,ipadx=50,ipady=10,sticky="e")

        #checkbox
        # it means that we will download a video high quality possible
        self.check_quality = Checkbutton(self.root, text="Best resolution")
        self.check_quality.grid(row=1, column=1)

        save_local_label = Label(self.root, width=15, text="Save Location", bg="blue").grid(row=2,column=0)
        self.save_local = Entry(self.root)
        self.save_local.grid(row=2,column=1,padx=15,pady=15,ipadx=50,ipady=10,sticky="e")
        


    # save file:
    # Open filedialog and return adress of save's location
    def find_direction(self):
        name_file = str(pafy.new(self.url.get()).title)
        location_file_save = asksaveasfilename(title="Save your video",parent=self.root,initialfile=name_file,filetypes=[('video files','.mp4'),('webm','.webm'),('all files','.*')])
        return location_file_save
    
    # get value save's location in Entry
    def get_value_from_button(self):
        self.adr = self.find_direction()
        self.save_local.delete(0, END)
        self.save_local.insert(0, str(self.adr))

    def download(self):
        video = pafy.new(self.url.get())
        # video.title 
        if self.check_quality['indicatoron'] == 1: #checkbox: whether best_resolution have clicked or not
            best = video.getbest()
        else:
            best = video.getbest(preftype="webm")
        return best.download(filepath=os.path.dirname(self.save_local.get()),quiet=False)
    

    def run_code(self):
        mainloop()
        



if __name__ == '__main__':
    app = App()
    if True:
        app.run_code()
    