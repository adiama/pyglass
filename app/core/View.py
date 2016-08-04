from tkinter import *

class View(Frame):
    def __init__(self, master = None):
        Frame.__init__(self, master)
        self.pack(fill = 'both', expand = True)
        self.background = Canvas(self)
        self.background.pack(fill = 'both', expand = True)

    def __del__(self):
        pass

    def fullscreen(self, b):
        self.master.attributes('-fullscreen', b)

    def kill(self):
        self.master.destroy()
