from tkinter import *
# Create a calculator class
class Calculator:

    def __init__(self, master):
        '''
        Dic: Define what to do on initialization
        '''

        # Assign reference to the main window of the application
        self.master = master

        # Add a name to our application
        master.title("Scientific calculator")
        master.title("Group Project")

        # Create a line where we display the equation
        self.equation = Entry(master, width=36, borderwidth=5)

        # Assign a position for the equation line in the grey application window
        self.equation.grid(row=0, column=0, columnspan=4, padx=10, pady=10)

        # Execute the .creteButton() method
        self.createButton()


