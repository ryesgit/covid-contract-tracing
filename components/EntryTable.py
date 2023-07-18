from tkinter import *
from tkinter import ttk
from typing import List, Callable
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

        for row in range(self._get_table_frame().grid_size()[1]):
            for column in range(self._get_table_frame().grid_size()[0]):
                self._get_table_frame().grid_rowconfigure(row, weight=1)
                self._get_table_frame().grid_columnconfigure(column, weight=1)
        # Set padding of frame
        self._get_table_frame().grid_configure(padx=5, pady=5)

        button = ttk.Button(self._get_table_frame(), text="Add Contact")
        button.grid(row=self._get_table_frame().grid_size()[1] + 1, column=0, columnspan=self._get_table_frame().grid_size()[0], sticky="W E")

    # Override the draw content method
    def _draw_content(self, headers: List[str]):
        '''
        Draws the content of the table.

        Parameters
        ----------
        content : List[List[str]]
            The content of the table.
            List[0] contains the headers of the table.
            List[1] contains the entry types of the table.
        '''
        for row, column_value in enumerate(self.__data[0]):
            entry_type: Entry | Scale | Spinbox
            entry_type = (self.__data[1])[row]

            # Instantiate the passed entry type
            entry = entry_type(self._get_table_frame())

            # Set entry's grid geometry
            entry.grid(row=row, column=1, sticky="W E")
    # Override draw headers method
    def _draw_headers(self, headers: List[str]):
        '''
        Draws the headers of the table.
        '''
        for idx, header in enumerate(self.__data[0]):
            label = ttk.Label(self._get_table_frame(), padding=5); label.grid(row=idx, column=0)
            label['text'] = header
        