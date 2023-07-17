from tkinter import *
from tkinter import ttk

from typing import List

class UI:
    def __init__(self) -> None:
        self.__master = Tk()
        self.__frame = ttk.Frame(self.__master)
        self.__frame.grid(row=0, column=0, sticky="N W E S")

        self.__display_headers("Name", "Age")
        user_data = read_json('contacts.json')
        self.__display_user_data(user_data)

        self.__master.mainloop()

    def __display_headers(self, *args):
        
        for idx, header in enumerate(args):
            label = ttk.Label(self.__frame, padding=5); label.grid(row=0, column=idx)
            label['text'] = header

    def __display_user_data(self, data: List[dict]):
        '''
        Draws the user data on the UI.

        Parameters
        ----------
        data : List[dict]
            A list of dictionaries containing user data.
        '''
        for idx, user in enumerate(data):
            label = ttk.Label(self.__frame, padding=5); label.grid(row=idx+1, column=0)
            label['text'] = data[user]['name']
            label = ttk.Label(self.__frame, padding=5); label.grid(row=idx+1, column=1)
            label['text'] = data[user]['age']

def read_json(path):
    '''
    Reads the sample JSON file and returns a list of dictionaries.
    '''
    import json
    with open(path, 'r') as f:
        data = json.load(f)
    return data