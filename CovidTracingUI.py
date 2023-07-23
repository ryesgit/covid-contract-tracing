from tkinter import *
from tkinter import ttk

from typing import List
from ContactsIO import ContactsIO
from components.Table import Table
from utils.user_data_helpers import convert_data_to_array

class UI:
    def __init__(self) -> None:
        self.__master = Tk()
        self.__master.title("Contact Tracing App")
        self.__master.columnconfigure(0, weight=1)
        self.__master.rowconfigure(0, weight=1)

        self.__frame = ttk.Frame(self.__master)
        self.__frame.grid(row=0, column=0, sticky="N W E S")
        self.__frame.grid_columnconfigure(0, weight=1)
        self.__frame.grid_rowconfigure(0, weight=1)

        self.__frame.configure(borderwidth=5, relief="sunken")

        self.__canvas = []
        self.__display_user_data()

        add_contact_button = ttk.Button(self.__frame, text="Add Contact", command=self.show_add_contact_form)
        add_contact_button.grid(row=self.__frame.grid_size()[1], column=0, columnspan=2, sticky="W E")

        
        search_contact_button = ttk.Button(self.__frame, text="Search Contact", command=self.show_search_contact_form)
        search_contact_button.grid(row=self.__frame.grid_size()[1], column=0, columnspan=2, sticky="W E")


        # Center the window
        center_window(self.__master)

        # Rerender canvas every time new user is created
        self.__master.bind("<<NewUserCreate>>", lambda event: self.__display_user_data)

        self.__master.mainloop()

    def __display_user_data(self):
        '''
        Draws the user data on the UI.

        Parameters
        ----------
        data : List[dict]
            A list of dictionaries containing user data.
        '''
        print(self.__canvas)
        # Clear canvas first
        if self.__canvas:
            self.__canvas.destroy()

        contacts_delegator = ContactsIO('contacts.json')
        self.__contacts = contacts_delegator.get_user_data()

        canvas = Canvas(self.__frame)
        canvas.grid(row=0, column=0, sticky="N W E S")

        self.__canvas = canvas

        scrollbar = Scrollbar(self.__frame, orient="vertical", command=canvas.yview)
        scrollbar.grid(row=0, column=1, sticky="N S E")
        canvas.configure(yscrollcommand=scrollbar.set)

        table_frame = ttk.Frame(canvas)
        table_frame.configure(borderwidth=5, relief="sunken")
        canvas.create_window((0, 0), window=table_frame, anchor="nw", tags="table_frame")
        Table(table_frame, self.__contacts.copy())

        # Get the width of the table frame
        width = get_widget_width(table_frame)

        canvas.configure(width=width)
        canvas.bind("<Configure>", lambda event: canvas.configure(scrollregion=canvas.bbox("all")))
        canvas.bind("<<NewUserCreate>>", lambda event: canvas.configure(scrollregion=canvas.bbox("all")))
        canvas.configure(scrollregion=canvas.bbox("all"))

        # Resize the canvas to fill 5 items from the frame

    def show_add_contact_form(self):
        '''
        Create a new window for the contact tracing form.
        '''
        from components.ContactsForm import ContactsForm
        contacts_form = ContactsForm(self.__master)

        # Center this window
        center_window(contacts_form.get_window())

    def show_search_contact_form(self):
        '''
        Creates a new window for the search contact form.
        '''
        from components.SearchContactsForm import SearchContactsForm

        search_contacts_form = SearchContactsForm(self.__master, self.__contacts)

         # Center this window
        center_window(search_contacts_form.get_window())

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

def get_widget_width(widget):
    widget.update_idletasks()

    return widget.winfo_reqwidth()