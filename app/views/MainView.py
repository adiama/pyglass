# -*- coding: utf-8 -*-

from tkinter import *

from app.core.View import View

class MainView(View):
    def __call__(self, master = None):
        View.__init__(self, master)
        self.master.minsize(320, 160)
        self.master.geometry("1280x720")
        self.master.title("PyGlass")

        self.menubar = Menu(self)

        menu = Menu(self.menubar, tearoff = 0)
        self.menubar.add_cascade(label = "Window", menu = menu)
        menu.add_command(label = "Fullscreen Mode",
                         command = lambda: self.fullscreen(True))
        menu.add_command(label = "Windowed Mode",
                         command = lambda: self.fullscreen(False))

        menu = Menu(self.menubar, tearoff = 0)
        self.menubar.add_cascade(label = "Help", menu = menu)
        menu.add_command(label = "About",
                         command = lambda: self.new_view("About",
                                                         "initialize",
                                                         self.master))

        self.master.config(menu = self.menubar)
