from tkinter import *
from tkinter.filedialog import * 
from tkinter.messagebox import *
import pafy
import os

class App(Frame):
    def __init__(self, master=None):
        Frame.__init__(self, master)
        self.master.title("Download Youtube")

        # Entry and label
        self.label_url = Label(self.master, width=15, text="Link Video")
        self.label_url.grid(row=0,column=0,padx=15,pady=15)
        self.url = Entry(self.master)
        self.url.grid(row=0,column=1,padx=15,pady=15,ipadx=50,ipady=10,sticky="e")

        # Entry for place's informations of video
        Label(self.master, width=15, text="Title Video").grid(row=1,column=0,padx=15,pady=15)
        self.title_video = Entry(self.master)
        self.title_video.grid(row=1,column=1,padx=15,pady=15, sticky="w")

        Label(self.master, width=15, text="video's duration").grid(row=2,column=0,padx=15,pady=15)
        self.video_duration = Entry(self.master)
        self.video_duration.grid(row=2,column=1,padx=15,pady=15, sticky="w")

        # List quality of video like resolution and extension
        Label(self.master, width=15, text="Quality").grid(row=3,column=0,padx=15,pady=15)
        self.listCon = StringVar()
        self.list_quality = Listbox(self.master, listvariable=self.listCon)
        self.current_chosen = self.list_quality.curselection() #return tuple empty
        self.background_row = 'white'
        self.current_chosen_design = ""
        # print(self.current_chosen)
        self.list_quality.bind("<Double-Button-1>", self.OnDouble)
        self.list_quality.grid(row=3,column=1,padx=15,pady=15, sticky="w")

        # checkbox
        # it means that we will download version audio
        self.spamVar = StringVar()
        self.check_audio = Checkbutton(self.master, text="Audio", variable=self.spamVar, onvalue='Yes', offvalue='No')
        self.check_audio.grid(row=6, column=1)

        Label(self.master, width=15, text="Save Location").grid(row=5,column=0,padx=15,pady=15)
        self.save_local = Entry(self.master)
        self.save_local.grid(row=5,column=1,padx=15,pady=15,ipadx=50,ipady=10,sticky="e")

        # Progress bar
        # self.pb_label =Label(self.master, width=15, text="")
        # self.pb_label.grid(row=6,column=0,padx=15,pady=15)
        # self.pb = ttk.Progressbar(self.master, orient="horizontal", length=200, mode="determinate")
        # self.pb.grid(row=6, column=1, pady=15)

        #download's infor
        self.dl_info = Label(self.master, width=15, text="")
        self.dl_info.grid(row=7,column=1,padx=15,pady=15,ipadx=50)

        # button to display informations of video
        self.b4 = Button(self.master, text='show detail', command=self.show_information)
        self.b4.bind("<Button-1>", self.loading)
        self.b4.grid(row=0, column=3,padx=15,pady=15)
        # button open window to save file
        self.b3 = Button(self.master, text='Save', command=self.save_direction)
        self.b3.grid(row=5, column=3,padx=15,pady=15)
        # button download
        self.b1 = Button(self.master, text="Download", state="disabled", command=self.download)
        self.b1.bind('<Button-1>', self.downloading)
        self.b1.grid(row=8,column=1,padx=15,pady=15,sticky="w")
        
        # button quit
        self.b2 = Button(self.master, text='Quit', command=self.master.quit)
        self.b2.grid(row=8,column=1,padx=15,pady=15,sticky="e")

        # select to download Video or Audio on Youtube
        # self.select_video = Button(self.master, text="Download Video", command=Video)
        # self.select_video.grid(row=8,column=0,padx=15,pady=15,sticky="w")

        # self.select_audio = Button(self.master, text="Download Audio", command=Audio)
        # self.select_audio.grid(row=8,column=1,padx=15,pady=15,sticky="w")

    # function decorator:
    def download_active(func):
        def inner(self, *args):
            self.b1['state'] = 'normal'
            return func(self, *args)
        return inner

    def progress_bar(func):
        def inner(self, *args):
            func(self, *args)
            self.dl_info['text'] = "Xong rồi - Done !"
        return inner

    def loading(self, event):
        self.dl_info['text'] = "Đang nạp - Loading..."
    
    def downloading(self, event):
        self.dl_info['text'] = "Đang tải - Downloading..."

    # save file:
    # Open filedialog and return adress of save's location
    def save_direction(self):
        name_file = str(pafy.new(self.url.get()).title) 
        # title's video of url, this variable to set initially a name of file
        location_file_save = asksaveasfilename(title="Save your video",parent=self.master,initialfile=name_file,filetypes=[('all files','.*')])
        if location_file_save != None:
            self.save_local.delete(0, END) # refresh to entry
            self.save_local.insert(END, str(location_file_save)) # set a content

    def show_information(self):
        try:
            url = self.video_url
            if self.spamVar.get() == 'No' or self.spamVar.get() == "" :
                quality = self.get_videos_streams  # array of video's quality
                # delete content current
                self.title_video.delete(0, END)
                self.video_duration.delete(0, END)
                self.list_quality.delete(1, len(quality))
                # replace by a new info of video
                self.title_video.insert(0, str(url.title))
                self.video_duration.insert(0, str(url.duration))

                # # we can insert contents with method "insert()"
                # for i in range(len(quality)):
                #     self.list_quality.insert(i+1,(quality[i].resolution, quality[i].extension))

                # set content by method listvariable in Listbox
                # listCon.set('Un deux trois') sends 3 rows
                # listCon.get() will send to a array
                self.listCon.set(" ".join((str(quality[i].resolution) +"----"+ str(quality[i].extension)) for i in range(len(quality))))
                self.b1['state'] = 'disabled'
                self.dl_info['text'] = "Xong rồi - Done !"
            elif self.spamVar.get() == 'Yes':
                quality = self.get_audios_streams
                self.title_video.delete(0, END)
                self.video_duration.delete(0, END)
                self.list_quality.delete(1, len(quality))

                # replace by a new info of video
                self.title_video.insert(0, str(url.title))
                self.video_duration.insert(0, str(url.duration))
                self.listCon.set(" ".join((str(quality[i].extension)) for i in range(len(quality))))
                self.b1['state'] = 'disabled'
                self.dl_info['text'] = "Xong rồi - Done !"

                
        except ValueError as e:
            reponse = askokcancel("Url empty!!!","Please entry url!")
            if reponse:
                Video()     
            else:
                self.dl_info['text'] = "Error !!!"
    @download_active
    def OnDouble(self, event):
        widget = event.widget
        if self.current_chosen == (): # tuple empty in initial, so it must be get a row chosen by double click on listbox
            self.current_chosen = widget.curselection()
            # print(self.current_chosen)
        else:
            widget.itemconfig(index=self.current_chosen[0],background="white") # set a background = white in row selected before
            # widget.itemconfig(index=self.current_chosen[0],background="white")
            self.current_chosen = widget.curselection() # return a index chosen by a tuple in quality's listbox 
            # print(self.current_chosen)
            # value = widget.get(self.curent_chosen[0])
            # print ("selection:", selection, ": '%s'" % value)
        widget.itemconfig(index=self.current_chosen[0],background="red") # set a background = red in row selected currently

    @property
    def video_url(self):
        return pafy.new(self.url.get())

    @property
    def get_videos_streams(self):
        url = self.video_url
        videos = url.streams # method of pafy to show all quality's video possible, it return a array
        return videos

    @property
    def get_audios_streams(self):
        url = self.video_url
        audios = url.audiostreams # method of pafy to show all quality's video possible, it return a array
        return audios

    @progress_bar
    def download(self):
        if self.spamVar.get() == 'No':
            choice = self.get_videos_streams
        elif self.spamVar.get() == 'Yes':
            choice = self.get_audios_streams
        video_quality_selected = choice[self.current_chosen[0]]
        filename = video_quality_selected.download(filepath=os.path.dirname(self.save_local.get()),quiet=False)
    
    def run_code(self):
        mainloop()
        
        
class Video(App):
    def __init__(self, *args, **kwargs):
        App.__init__(self, *args, **kwargs)

class Audio(App):
    def __init__(self, *args, **kwargs):
        App.__init__(self, *args, **kwargs)
        self.label_url['text'] = "Link Audio"

if __name__ == '__main__':
    app = Video()
    app.run_code()
    