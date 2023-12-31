from tkinter import *
from tkinter import ttk
from typing import List, Callable
from utils.user_data_helpers import convert_data_to_array

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
        headers = data[0]
        self._draw_headers(headers)

        # Remove first element from data
        del data[0]
        self._draw_content(data)

    def _draw_headers(self, headers: List[str]):
        '''
        Draws the headers of the table.
        '''
        for idx, header in enumerate(headers):
            label = ttk.Label(self.__table_frame, padding=5); label.grid(row=0, column=idx, sticky="N E W S")
            label.configure(borderwidth=2, font="bold", relief="solid", anchor="center")
            label['text'] = header

    def _draw_content(self, content: List[List[str]]):

        '''
        [
            ["Ako", "12"],
            ["Siiya", "13"]
        ]
        
        '''
        for row, row_value in enumerate(content):
            for column, column_value in enumerate(row_value):

                color = "blue" if row % 2 == 0 else "white"
                text_color = "white" if row % 2 == 0 else "black"

                label = ttk.Label(self.__table_frame, background=color, foreground=text_color, padding=5, anchor=CENTER); label.grid(row=row+1, column=column, sticky="W E")
                label.configure(borderwidth=2, relief="solid")
                label["text"] = column_value
                label.configure(anchor="center")

    def _get_table_frame(self):
        return self.__table_frame