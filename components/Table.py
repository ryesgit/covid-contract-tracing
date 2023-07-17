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
        self.__draw_headers(headers)

        # Remove first element from data
        del data[0]
        self.__draw_content(data)

    def __draw_headers(self, headers: List[str]):
        '''
        Draws the headers of the table.
        '''
        for idx, header in enumerate(headers):
            label = ttk.Label(self.__table_frame, padding=5); label.grid(row=0, column=idx)
            label['text'] = header

    def __draw_content(self, content: List[List[str]]):

        '''
        [
            ["Ako", "12"],
            ["Siiya", "13"]
        ]
        
        '''
        for row, row_value in enumerate(content):
            for column, column_value in enumerate(row_value):
                label = ttk.Label(self.__table_frame, padding=5); label.grid(row=row+1, column=column)
                label["text"] = column_value

    def _get_table_frame(self):
        return self.__table_frame