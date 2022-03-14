import tkinter
import tkinter 

class MYGUI:
    def __init__(self):
        self.main_window = tkinter.Tk()

        self.main_window.geometry('500x200')
        self.main_window.title("Label Demo")

        self.label1 = tkinter.Label(self.main_window,text='Hello World')

        self.label2 = tkinter.Label(self.main_window, text = 'This is my GUI Program')

        self.label1.pack(side='top')
        self.label2.pack( side = 'bottom')

        tkinter.mainloop()


my_gui = MYGUI()

print("moving on....")


