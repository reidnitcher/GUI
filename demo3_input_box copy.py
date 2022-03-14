import tkinter
import tkinter.messagebox

class kilo_converter:
    def __init__(self):
        self.main_window = tkinter.Tk()

        self.main_window.geometry('500x200')
        self.main_window.title('Frames and Buttons')

        """"
        self.kilo_entry = tkinter.entry(self.top_frame, width = 10)
        self.prompt_label = tkinter.label()

        self.prompt_label.pack(side = 'left')
        self.kilo_entry.pack(side = 'left')
        """


        self.top_frame = tkinter.Frame(self.main_window)
        self.bottom_frame = tkinter.Frame(self.main_window)
        
        self.top_frame.pack(side='top')
        self.bottom_frame.pack(side='top')


        self.calcbutton = tkinter.Button(self.main_window,text = 'Convert', command=self.convert)              

        self.quit_button = tkinter.Button(self.main_window, text = 'Quit', command = self.main_window.destroy)

        self.calcbutton.pack(side = 'left')
        self.quit_button.pack(side = 'right')

        tkinter.mainloop()

    def convert(self):
        kilo = float(self.kilo_entry.get())

        miles = kilo * 0.6214

        tkinter.messagebox.showinfo("Results,",
                                str(kilo) + 
                                'kilometers is equal to', 
                                str(miles) + ''


kilo_conv = kilo_converter()

print("moving on....")