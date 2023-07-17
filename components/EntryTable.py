from tkinter import *
from tkinter import ttk
from typing import List
from components.Table import Table

class EntryTable(Table):
    '''
    A table that allows the user to input data.

    Parameters
    ----------
    frame : ttk.Frame
        The frame to place the table on.
    data : List[dict]
        The data to display on the table.
    '''
    def __init__(self, frame: Frame, data: List[dict]):

        self.__data = data.copy()
        super().__init__(frame, data)
        self.__draw_content()
        button = ttk.Button(self._get_table_frame(), text="Add Contact")
        button.grid(row=2, column=0, columnspan=self._get_table_frame().grid_size()[0], sticky="W E")
    # Override the draw content method
    def __draw_content(self):
        '''
        Draws the content of the table.

        Parameters
        ----------
        content : List[List[str]]
            The content of the table.
        '''
        for column, column_value in enumerate(self.__data[0]):

            entry = ttk.Entry(self._get_table_frame()); entry.grid(row=1, column=column)
            entry.grid(padx=5, pady=5)

        