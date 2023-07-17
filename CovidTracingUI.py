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

        add_contact_button = ttk.Button(self.__frame, text="Add Contact", command=self.show_form_window)
        add_contact_button.grid(row=self.__frame.grid_size()[1], column=0, columnspan=2, sticky="W E")

        # Center the window
        center_window(self.__master)

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

    def show_form_window(self):
        '''
        Create a new window for the contact tracing form.
        '''
        self.__form_window = Toplevel(self.__master)
        self.__form_window.title("Contact Tracing Form")

        welcome = ttk.Label(self.__form_window, padding=5); welcome.grid(row=0, column=0)
        welcome['text'] = "Welcome to the Contact Tracing Form!"

        # Center this window
        center_window(self.__form_window)


def read_json(path):
    '''
    Reads the sample JSON file and returns a list of dictionaries.
    '''
    import json
    with open(path, 'r') as f:
        data = json.load(f)
    return data

def center_window(window: Tk | Toplevel):
        '''
        Parameters
        ----------
        window : Tk | Toplevel
            The window to center.
        '''
        window.update_idletasks()
        width = window.winfo_width()
        height = window.winfo_height()
        x = (window.winfo_screenwidth() // 2) - (width // 2)
        y = (window.winfo_screenheight() // 2) - (height // 2)
        window.geometry('{}x{}+{}+{}'.format(width, height, x, y))