from tkinter import *
from importlib import import_module

from app.core.Dispatcher import Dispatcher


class Controller(object):
    def __init__(self):
        self.dispatcher = Dispatcher()

    def render(self, view):
        module = import_module("app.views.%sView" % view[:-10])
        class_ = getattr(module, "%sView" % view[:-10])
        self.view = class_()

        if not self.__class__.__base__ in self.view.__class__.__bases__:
            self.view.__class__.__bases__ += (self.__class__.__base__, )

        self.view.dispatcher = Dispatcher()

    def new_view(self, class_, action, parent):
        master = Toplevel(parent)
        newView = self.dispatcher.dispatch(class_, action, master)
        newView.view.mainloop()
