from typing import List
from tkinter import *
from tkinter import ttk
from functools import partial
from ContactsIO import ContactsIO

from utils.gui_helpers import center_window

class SearchContactsForm:
    '''
    This module builds a form that searches for
    contacts available inside the repository of contacts
    provided by the application

    Methods
    -------
    search_by_category(category: str, options: dict) -> List[dict]
        Searches for contacts by category
        and retunts a list of contacts
        that match the category

    render_canvas(contacts: List[dict]) -> None
        Renders the canvas with the searched contacts
    '''
    def __init__(self, master, contacts_delegator: ContactsIO) -> None:
        '''
        Parameters
        ----------
        master
            This form's master widget
        contacts : List[dict]
            A list of dictionaries containing contacts data.
        contacts_delegator : ContactsIO
            The instance that talks to the contacts repository
        '''
        self.__master = master
        self.__contacts_delegator = contacts_delegator

        # Create the search contact form widget
        self.__form_window = Toplevel(master)
        self.__form_window.title("Search Contacts Form")


        title = ttk.Label(self.__form_window, text="Search Contacts Form", padding=5)
        title.grid(row=0, column=0, columnspan=2)

        # Create a canvas to place the table on
        self.__canvas = Canvas(self.__form_window)
        self.__canvas.grid(row=1, column=0, sticky="N W E S")

        # Create a frame to place searched entries
        self.__searched_entries_frame = ttk.Frame(self.__canvas)
        self.__searched_entries_frame.grid(row=0, column=0, sticky="N W E S")

        self.__contacts = self.__contacts_delegator.get_user_data()
        self.__draw_form()

    def __draw_form(self):
        '''
        Draws the search contact form
        '''
        from components.EntryTable import EntryTable

        if self.__contacts:
            # Set first contact's categories as default categories
            categories = []

            for key in self.__contacts[0]:
                categories.append(key)

            self.__headers = categories

            # Create combobox for each category
            combobox = partial(ttk.Combobox, values=categories, state="readonly")

            def display_searched_entries(options):
                self.render_canvas(self.search_by_category(options))

            EntryTable(self.__form_window, ["Category", "Value"], [combobox, ttk.Entry], on_submit=display_searched_entries)


    def search_by_category(self, options) -> List[dict]:
        '''
        Searches for contacts by category
        and returns a list of contacts
        that match the category

        Parameters
        ----------
        category : str
            The category to search for
        options : dict
            Options to search for.
            Includes 'Category' and 'Value' properties

        Returns
        -------
        List[dict]
            A list of contacts that match the category
        '''
        return self.__contacts_delegator.get_users_by_category(options)
    
    def render_canvas(self, contacts: List[dict]) -> None:
        '''
        Display searched entries onto the frame inside the canvas
        '''
        from components.Table import Table

        if self.__canvas:
            self.__canvas.destroy()

        self.__form_window.geometry("")
        
        self.__canvas = Canvas(self.__form_window)
        self.__canvas.grid(row=1, column=0, sticky="N W E S")

        self.__searched_entries_frame = ttk.Frame(self.__canvas)
        self.__searched_entries_frame.grid(row=0, column=0, sticky="N W E S")

        self.__searched_entries_frame.bind("<Configure>", lambda event: self.__canvas.configure(scrollregion=self.__canvas.bbox("all"), width=event.width, height=event.height))

        Table(self.__searched_entries_frame, contacts)

        for child in self.__canvas.winfo_children():
            self.__canvas.create_window(0, 0, anchor="nw", window=child)

        center_window(self.__form_window)

    def get_window(self):
        return self.__form_window