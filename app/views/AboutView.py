# -*- coding: utf-8 -*-

from tkinter import *

from app.core.View import View

class AboutView(View):
    def __call__(self, master = None):
        View.__init__(self, master)
        self.master.minsize(480, 320)
        self.master.maxsize(480, 320)
        self.master.title("About")
