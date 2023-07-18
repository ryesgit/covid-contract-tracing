from tkinter import *
from tkinter import ttk

from functools import partial

class ContactsForm:
    '''
    Top level window asking the user details for contact tracing.

    Parameters
    ----------
    master: Tk
        The parent window of this window.
    '''

    def __init__(self, master: Tk) -> None:
        self.__form_window = Toplevel(master)
        self.__form_window.title("Contact Tracing Form")

        welcome = ttk.Label(self.__form_window, padding=5); welcome.grid(row=0, column=0)
        welcome['text'] = "Welcome to the Contact Tracing Form!"
        self.draw_form()

    def get_window(self):
        return self.__form_window
    
    def draw_form(self):
        from components.EntryTable import EntryTable

        # Create entry types of the table and define
        # some of their arguments
        entry_types = [Entry, partial(ttk.Spinbox, from_=0, to=100)]
        headers = [["Name", "Age"], entry_types]
        EntryTable(self.__form_window, headers)