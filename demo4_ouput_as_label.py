import tkinter
import tkinter.messagebox
from traceback import TracebackException

class kilo_converter:
    def __init__(self):
        self.main_window = tkinter.Tk()

        self.top_frame = tkinter.Frame(self.main_window)
        self.bottom_frame = tkinter.Frame(self.main_window)
        self.mid_frame = tkinter.Frame(self.main_window)


        self.top_frame.pack(side='top')
        self.mid_frame.pack(side = 'top')
        self.bottom_frame.pack(side='top')

        self.prompt_label = tkinter.Label(self.top_frame,
            text = "Enter a distance in kilometers:")

        self.kilo_entry = tkinter.Entry(self.top_frame, width = 10)

        self.prompt_label.pack(side = 'left')
        self.kilo_entry.pack(side = 'left')

        self.descr_label = tkinter.Label(self.mid_frame,
                                            text = "Converted to Miles:")
                                            
        self.miles_var = tkinter.StringVar()

        self.miles_label = tkinter.Label(self.mid_frame,
                                            textvariable=self.miles_var)
        

        self.calcbutton = tkinter.Button(self.main_window,text = 'Convert', command=self.convert)              
        self.quit_button = tkinter.Button(self.main_window, text = 'Quit', command = self.main_window.destroy)

        self.calcbutton.pack(side = 'left')
        self.quit_button.pack(side = 'right')

        tkinter.mainloop()

    def convert(self):
        kilo = float(self.kilo_entry.get())

        miles = kilo * 0.6214

        self.miles_var.set(miles)


kilo_conv = kilo_converter()

print("moving on....")