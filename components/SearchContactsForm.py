from typing import List
from tkinter import *
from tkinter import ttk
from functools import partial

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

        self.__draw_form()

    def __draw_form(self):
        '''
        Draws the search contact form
        '''
        from components.EntryTable import EntryTable

        if self.__contacts:
            # Set first contact's categories as default categories
            categories = []
            print(self.__contacts)
            for key in self.__contacts[0]:
                categories.append(key)

            self.__headers = categories

            # Create combobox for each category
            combobox = partial(ttk.Combobox, values=categories, state="readonly")


            EntryTable(self.__form_window, ["Category", "Value"], [combobox, ttk.Entry], on_submit=self.search_by_category)

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
        print(f"options: {options}")
        print(f"Category: {options['Category']}")
        contacts = []
        for contact in self.__contacts:

            property_index = self.__headers.index(options['Category'])

            if contact[property_index] == options['Value']:
                contacts.append(contact)

        print(contacts)
        return contacts
    

    def get_window(self):
        return self.__form_window