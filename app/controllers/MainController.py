# -*- coding: utf-8 -*-

from tkinter import *

from app.controllers.AppController import AppController

class MainController(AppController):
    def __init__(self):
        self.render(self.__class__.__base__.__name__)

    def initialize(self, parent = None):
        #-----------------
        #Your code here...
        #-----------------
        self.view(parent)
        self.view.mainloop()
