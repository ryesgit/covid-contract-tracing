from tkinter import *
from tkinter import ttk
from typing import List, Callable
from components.Table import Table
from functools import partial

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
    def __init__(self, frame: Frame, headers: List[str], entry_types: List[Callable] | List[List[Callable]], on_submit: Callable = None):

        self.__entries = []
        self.__headers = headers
        super().__init__(frame, [headers, entry_types])


        for row in range(self._get_table_frame().grid_size()[1]):
            for column in range(self._get_table_frame().grid_size()[0]):
                self._get_table_frame().grid_rowconfigure(row, weight=1)
                self._get_table_frame().grid_columnconfigure(column, weight=1)


        # Set padding of frame
        self._get_table_frame().grid_configure(padx=5, pady=5)
        

        button = ttk.Button(self._get_table_frame(), text="Submit", command=lambda: on_submit(self.consolidate_info()))
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
        for row, column_value in enumerate(headers[0]):
            entry_type: Entry | Scale | Spinbox
            entries = headers[0]
            entry_type = (entries)[row]

            # If it is a list of entry types, iterate through each
            if type(entry_type) == list:

                entries_frame = ttk.Frame(self._get_table_frame(), padding=5)
                entries_frame.grid(row=row, column=1, sticky="W E")

                for idx, entry in enumerate(entry_type):

                    entry = entry(entries_frame)

                    # Add to entries list
                    self.__entries.append(entry)

                    entry.grid(row=idx, column=1, sticky="W E")
                continue
            # Instantiate the passed entry type

            entry = entry_type(self._get_table_frame())

            # Add to entries list
            self.__entries.append(entry)

            # Set entry's grid geometry
            entry.grid(row=row, column=1, sticky="W E")

    # Override draw headers method to write headers vertically
    def _draw_headers(self, headers: List[str]):
        '''
        Draws the headers of the table.
        '''
        for idx, header in enumerate(headers):
            label = ttk.Label(self._get_table_frame(), padding=5); label.grid(row=idx, column=0)
            label['text'] = header

        ttk.Separator(self._get_table_frame(), orient=VERTICAL).grid(row=0, column=0, rowspan=len(headers), sticky="E N S")

    def consolidate_info(self):
        '''
        Consolidates the gathered from the entries of the table.
        '''
        entry_values = []

        for entry in self.__entries:

            if type(entry) == ttk.Radiobutton:
                try:
                    radio_value = entry.getvar(entry.cget("variable"))
                    entry_values.append("Yes" if radio_value == 1 else "No")
                except:
                    print("Radiobutton value not selected")
                    entry_values.append("")
                finally:
                    continue
            #     if type(entry["variable"]) == str:
            #         continue
            #     var_name = entry.cget("variable")

            #     radio_button_value = entry.getvar(var_name)

            #     if radio_button_value == 0:
            #         entry_values.append("No")
            #         continue

            #     else:
            #         entry_values.append("Yes")
            #         continue

            entry_values.append(entry.get())

        # Turn the list of headers and list of entries to a key-value pair
        entry_values = dict(zip(self.__headers, entry_values))
        print(entry_values)
        return entry_values
        