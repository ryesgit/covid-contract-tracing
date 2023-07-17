from tkinter import *
from tkinter import ttk
from typing import List, Callable

class Table:
    '''
    Utilizes the TK library to create a table of data.
    '''
    def __init__(self, frame: ttk.Frame, data: List[dict]):
        '''
        Parameters
        ----------
        frame : ttk.Frame
            The frame to place the table on.
        headers : List[str]
            The headers of the table.
        data : List[dict]
            The data to display on the table.
        '''
        self.__table_frame = ttk.Frame(frame); self.__table_frame.grid(row=0, column=0, sticky="N W E S")
        self.__headers = [attribute for attribute in data[list(data.keys())[0]]]
        self.__draw_headers()
        self.__data = data
        self.__draw_user_data()

    def __draw_headers(self):
        '''
        Draws the headers of the table.
        '''
        for idx, header in enumerate(self.__headers):
            label = ttk.Label(self.__table_frame, padding=5); label.grid(row=0, column=idx)
            label['text'] = header

    def __draw_user_data(self):
        for row, user in enumerate(self.__data):
            for column in range(len(self.__headers)):
                label = ttk.Label(self.__table_frame, padding=5); label.grid(row=row+1, column=column)
                label["text"] = self.__data.get(user, '').get(self.__headers[column], '')