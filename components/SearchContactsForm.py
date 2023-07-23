from typing import List
from tkinter import *
from tkinter import ttk

class SearchContactsForm:
    '''
    This module builds a form that searches for
    contacts available inside the repository of contacts
    provided by the application

    Methods
    -------
    search_by_category(category: str) -> List[dict]
        Searches for contacts by category
        and retunts a list of contacts
        that match the category

    rerender_canvas(contacts: List[dict]) -> None
        Rerenders the canvas with the newly searched contacts
    '''
    def __init__(self, master, contacts: List[dict]) -> None:
        '''
        Parameters
        ----------
        master
            This form's master widget
        contacts : List[dict]
            A list of dictionaries containing contacts data.
        '''
        self.__master = master
        self.__contacts = contacts

        # Create the search contact form widget
        self.__form_window = Toplevel(master)
        self.__form_window.title("Search Contacts Form")

        title = ttk.Label(self.__form_window, text="Search Contacts Form", padding=5)
        title.grid(row=0, column=0, columnspan=2)

    def get_window(self):
        return self.__form_window