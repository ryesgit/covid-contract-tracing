from ContactsIO import ContactsIO
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

    def __init__(self, master: Tk, contacts_delegator: ContactsIO) -> None:

        self.__contacts_delegator = contacts_delegator

        self.__master = master
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

        been_with_diagnosed = BooleanVar()
        diagnosis_radiobuttons = [partial(ttk.Radiobutton, text="Yes", variable=been_with_diagnosed, value=True), \
                                  partial(ttk.Radiobutton, variable=been_with_diagnosed, text="No", value=False)]

        entry_types = [Entry, partial(ttk.Spinbox, from_=0, to=100), Entry, \
                      vaccination_combobox, diagnosis_radiobuttons]
        

        headers = ["Name", "Age", "Address","Vaccination Status", "Have you been in contact\nwith someone diagnosed with COVID?"]
        EntryTable(self.__form_window, headers, entry_types, on_submit=self.submit_form)

    def submit_form(self, user_data):

        # Write the user data to the json file
        self.__contacts_delegator.write_user_data(user_data)
        # Close the window
        self.__master.event_generate("<<NewUserCreate>>")
        self.__form_window.destroy()