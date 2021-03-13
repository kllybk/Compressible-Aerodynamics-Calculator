"""
A list of individuals who made a significant contribution to this code are provided
below:
Brian
Taylor
Musfique

An example of object oriented programming, there are other ways to
organize and write this. But this is how I am familiar with doing it.

"""
import tkinter as tk
from tkinter import ttk, messagebox

__version__ = 'BETA'


class MainApplication:

    """
        This class will hold all of the instances of any other classes we
        may use for the calculator
        It is also responsible for defining the main window of the application

    """

    def __init__(self, master):

        # ##### Master window (root) ##### #
        self.master = master
        self.w = 1500
        self.h = 600
        self.master.geometry('{}x{}+0+0'.format(self.w, self.h))
        # self.master.state('zoomed')  # full screen
        self.master.title('Compressible-Aerodynamics-Calculator')

        # ##### Fonts & Styles ##### #
        self.text_font = "-family {Times New Roman} -size 12"
        self.title_font = "-family {Times New Roman} -size 18"
        self.background_color = "lightblue"  # can also use hex colors
        self.style = ttk.Style()
        self.style.theme_use('winnative')  # only supported by windows os
        self.master.configure(background=self.background_color)

        # ##### Instantiate the Different Frames ##### #
        isenflow = IsentropicFlowFrame(master=self.master,
                                       background_color='pink',
                                       title_font=self.title_font,
                                       text_font=self.text_font)

        # ##### Grid Everything ##### #
        isenflow.frame.grid()


class IsentropicFlowFrame:
    """
        This class will hold everything associated with the Isentropic
        Flow Relations and will be called in the __init__ of MainApp.

    """
    def __init__(self, master, background_color, title_font, text_font):
        self.master = master  # a place to live
        # this frame will hold all of the entries and output
        self.frame = tk.Frame(master=self.master,
                              bg=background_color)

        self.title = tk.Label(master=self.frame,
                              text='Isentropic Flow Relations',
                              font=title_font,
                              bg=background_color)

        inputs = ['Mach number', 'T/T0', 'p/p0']
        self.input = tk.StringVar()
        self.input.set(inputs[0])
        # optionMenu()s can't take keyword arguments for some reason
        input_menu = tk.OptionMenu(self.frame,  # = master
                                   self.input,  # = variable
                                   command=self.print_input,
                                   *inputs)  # = list of options

        # ##### Grid ##### #
        self.title.grid(row=0, column=0)
        input_menu.grid(row=1, column=0)

    def print_input(self, *args):
        """ *args is necessary for some reason or else the compiler will
         complain """
        # tk.StringVar()s need to use the .get()/.set() methods
        print(self.input.get())


# this only executes if this .py file is being run directly
if __name__ == "__main__":
    # tkinter loop
    root = tk.Tk()
    app = MainApplication(root)
    root.mainloop()













