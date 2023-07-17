from tkinter import *
from tkinter import ttk

from typing import List
from ContactsIO import ContactsIO
from components.Table import Table
from utils.user_data_helpers import convert_data_to_array

class UI:
    def __init__(self) -> None:
        self.__master = Tk()
        self.__frame = ttk.Frame(self.__master)
        self.__frame.grid(row=0, column=0, sticky="N W E S")

        headers = ["Name", "Age"]

        # Initialize contacts delegator
        contacts_delegator = ContactsIO('contacts.json')

        user_data = contacts_delegator.get_user_data()
        self.__display_user_data(user_data)

        add_contact_button = ttk.Button(self.__frame, text="Add Contact", command=self.show_form_window)
        add_contact_button.grid(row=self.__frame.grid_size()[1], column=0, columnspan=2, sticky="W E")

        # Center the window
        center_window(self.__master)

        self.__master.mainloop()

    def __display_user_data(self, data: List[dict]):
        '''
        Draws the user data on the UI.

        Parameters
        ----------
        data : List[dict]
            A list of dictionaries containing user data.
        '''
        data = convert_data_to_array(data)
        table = Table(self.__frame, data)

        # for idx, user in enumerate(data):
        #     label = ttk.Label(self.__frame, padding=5); label.grid(row=idx+1, column=0)
        #     label['text'] = data[user]['name']
        #     label = ttk.Label(self.__frame, padding=5); label.grid(row=idx+1, column=1)
        #     label['text'] = data[user]['age']

    def show_form_window(self):
        '''
        Create a new window for the contact tracing form.
        '''
        from components.ContactsForm import ContactsForm
        contacts_form = ContactsForm(self.__master)

        # Center this window
        center_window(contacts_form.get_window())

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