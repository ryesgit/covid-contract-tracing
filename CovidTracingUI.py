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

        self.__display_user_data()

        add_contact_button = ttk.Button(self.__frame, text="Add Contact", command=self.show_form_window)
        add_contact_button.grid(row=self.__frame.grid_size()[1], column=0, columnspan=2, sticky="W E")

        # Center the window
        center_window(self.__master)

        self.__master.bind("<<NewUserCreate>>", lambda event: self.rerender_screen())

        self.__master.mainloop()

    def __display_user_data(self):
        '''
        Draws the user data on the UI.

        Parameters
        ----------
        data : List[dict]
            A list of dictionaries containing user data.
        '''
        
        for child in self.__frame.winfo_children():
             child.destroy()

        contacts_delegator = ContactsIO('contacts.json')
        data = contacts_delegator.get_user_data()


        
        canvas = Canvas(self.__frame)
        canvas.grid(row=0, column=0, sticky="N W E S")

        scrollbar = Scrollbar(self.__frame, orient="vertical", command=canvas.yview)
        scrollbar.grid(row=0, column=1, sticky="N S E")
        canvas.configure(yscrollcommand=scrollbar.set)

        table_frame = ttk.Frame(canvas)
        table_frame.configure(borderwidth=5, relief="sunken")
        canvas.create_window((0, 0), window=table_frame, anchor="nw", tags="table_frame")
        Table(table_frame, data)
        canvas.configure(width=250)
        
        canvas.bind("<Configure>", lambda event: canvas.configure(scrollregion=canvas.bbox("all")))
        canvas.configure(scrollregion=canvas.bbox("all"))


        # Resize the canvas to fill 5 items from the frame

    def show_form_window(self):
        '''
        Create a new window for the contact tracing form.
        '''
        from components.ContactsForm import ContactsForm
        contacts_form = ContactsForm(self.__master)

        # Center this window
        center_window(contacts_form.get_window())

    def rerender_screen(self):
        print("Screen rerender")
        self.__display_user_data()
        add_contact_button = ttk.Button(self.__frame, text="Add Contact", command=self.show_form_window)
        add_contact_button.grid(row=self.__frame.grid_size()[1], column=0, columnspan=2, sticky="W E")

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