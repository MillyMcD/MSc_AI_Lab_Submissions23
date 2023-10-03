import tkinter as tk

class Simple_Calculator:
    """
    This is the Simple_Calculator - it has a starting value of 0.0,
    a user can input a variable (float) to subtract or add on to
    the starting value, which is known as running_total. This can
    also be reset with the 'reset' button and the widget can be
    exited with the 'Quit' button

    Usage: 
        gui = Simple_Calculator () 
    """

    def __init__(self): #initilisation function
        self.mw = tk.Tk()  #create main window
        self.mw.title("Simple Calculator")  #set the title of the main window

        self.top_frame = tk.Frame(self.mw) #create three frames in the main window, that will group different widgets
        self.mid_frame = tk.Frame(self.mw)
        self.bottom_frame = tk.Frame(self.mw)

        #create the widgets for the top frame
        self.total_label = tk.Label(self.top_frame, text = "Total:")
        self.result = tk.StringVar()
        self.result_label = tk.Label(self.top_frame,textvariable=self.result)

        self.total_label.pack(side = "left")
        self.result_label.pack(side = "right") #at this point the top line is finished

        self.temp_entry = tk.Entry(self.mid_frame,width = 15)

        self.temp_entry.pack() #at this point the middle line is finished

        self.add_button = tk.Button(self.bottom_frame, text = "+", command = self.addition) #adding buttons to widget
        self.sub_button = tk.Button(self.bottom_frame, text = "-", command = self.subtraction)
        self.reset_button = tk.Button(self.bottom_frame, text = "Reset", command = self.reset)
        self.quit_button = tk.Button(self.bottom_frame, text = "Quit", command = self.mw.destroy)

        #pack the buttons for bottom window
        self.add_button.pack(side = "left")
        self.sub_button.pack(side = "left")
        self.quit_button.pack(side = "right")
        self.reset_button.pack(side = "right")

        #ensuring the running total displays as 0.0 when started
        self.reset()

        self.top_frame.pack()#packing each frame into the GUI
        self.mid_frame.pack()
        self.bottom_frame.pack()

        tk.mainloop() #renders the GUI into existance

    def addition(self): 
        """
        this is the addition function - this gets the value from the temp_entry
        and adds it to the running total, updating the result
        """
        value = float(self.temp_entry.get())
        self.running_total += value
        self.result.set(self.running_total)

    def subtraction(self):
        """
        this is the subtraction function - this gets the value from the temp_entry
        and subtracts it from the running total, updating the result
        """
        value = float(self.temp_entry.get())
        self.running_total -= value
        self.result.set(self.running_total)

    def reset(self):
        """
        this is the reset function - resets running_total back to a float (0.0)
        """
        self.running_total = 0.0
        self.result.set(self.running_total)

gui = Simple_Calculator () 
