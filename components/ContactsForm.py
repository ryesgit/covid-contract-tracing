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

        vaccination_statuses = ["None", "1st Dose", "2nd Dose", "1st Booster Shot", "2nd Booster Shot"]
        vaccination_combobox = partial(ttk.Combobox, values=vaccination_statuses, state="readonly")

        been_with_diagnosed = StringVar()
        diagnosis_radiobuttons = [partial(ttk.Radiobutton, text="Yes", variable=been_with_diagnosed, value=True), \
                                  partial(ttk.Radiobutton, variable=been_with_diagnosed, text="No", value=False)]

        entry_types = [Entry, partial(ttk.Spinbox, from_=0, to=100), Entry, \
                      vaccination_combobox, diagnosis_radiobuttons]
        
        headers = [["Name", "Age", "Address","Vaccination Status", "Have you been in contact\nwith someone diagnosed with COVID?"], entry_types]
        EntryTable(self.__form_window, headers)