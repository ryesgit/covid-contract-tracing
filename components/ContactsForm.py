from tkinter import *
from tkinter import ttk

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

    def get_window(self):
        return self.__form_window