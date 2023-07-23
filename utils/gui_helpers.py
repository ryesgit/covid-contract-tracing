from tkinter import Tk, Toplevel

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

