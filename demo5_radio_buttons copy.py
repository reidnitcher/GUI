import tkinter
import tkinter.messagebox

class radio_box:
    def __init__(self):
        self.main_window = tkinter.Tk()

        self.top_frame = tkinter.Frame(self.main_window)
        self.bottom_frame = tkinter.Frame(self.main_window)

        self.top_frame.pack(side='top')
        self.bottom_frame.pack(side='top')
       
        self.radio_var = tkinter.IntVar()

        #SET THE intvar object to 1

        self.radio_var.set(10)

        self.rb1 = tkinter.Radiobutton(self.top_frame, 
                                        text = 'Option1', 
                                        variable=self.radio_var, 
                                        value=1)
        self.rb2 = tkinter.Radiobutton(self.top_frame, 
                                        text = 'Option2', 
                                        variable=self.radio_var, 
                                        value=2)
        self.rb3 = tkinter.Radiobutton(self.top_frame, 
                                        text = 'Option3', 
                                        variable=self.radio_var, 
                                        value=3)
        self.rb2.select()
        
        self.rb1.pack()
        self.rb2.pack()
        self.rb3.pack()
       
        #pack the frames

        self.okbutton = tkinter.Button(self.main_window,text = 'OK', command=self.show_choice)              
        self.reset = tkinter.Button(self.main_window, text = 'Reset', command =self.rb1.select)
        self.quitbutton = tkinter.Button(self.main_window,text= 'Quit', command=self.main_window.destroy)

        self.okbutton.pack(side = 'left')
        self.reset.pack(side = 'left')
        self.quitbutton.pack(side = 'left')
        
        self.top_frame.pack(side='top')
        self.bottom_frame.pack(side='top')
        
        tkinter.mainloop()

    def show_choice(self):
        tkinter.messagebox.showinfo("Selection", 'You have selected option ' + str(self.radio_var.get()))

mygui = radio_box()

print("moving on....")