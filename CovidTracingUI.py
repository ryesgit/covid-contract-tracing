from tkinter import *
from tkinter import ttk

from typing import List

class UI:
    def __init__(self) -> None:
        self.__master = Tk()
        self.__frame = ttk.Frame(self.__master)
        self.__frame.grid(row=0, column=0, sticky="N W E S")

        self.__display_headers("Name", "Age")
        self.__master.mainloop()

    def __display_headers(self, *args):
        
        for idx, header in enumerate(args):
            label = ttk.Label(self.__frame, padding=5); label.grid(row=0, column=idx)
            label['text'] = header