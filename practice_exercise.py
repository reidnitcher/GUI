import tkinter

class average_grade:
    def __init__(self):
        self.main_window = tkinter.Tk()

        self.top_frame = tkinter.Frame(self.main_window)
        self.mid_frame = tkinter.Frame(self.main_window)
        self.bottom_frame = tkinter.Frame(self.main_window)

        self.top_frame.pack(side='top')
        self.bottom_frame.pack(side='top')
        self.bottom_frame.pack(side='top')

        self.score1_label = tkinter.Label(self.top_frame,
            text = "Enter the score for test 1:")
        self.score2_label = tkinter.Label(self.top_frame,
            text = "Enter the score for test 2:")
        self.score3_label = tkinter.Label(self.top_frame,
            text = "Enter the score for test 3:")
        self.average_label = tkinter.Label(self.main_window,
            text='Average')
        self.avg_score = tkinter.Label(self.main_window,
            text='avergae')
        

        self.score1_entry = tkinter.Entry(self.top_frame, width = 10)
        self.score2_entry = tkinter.Entry(self.top_frame, width = 10)
        self.score3_entry = tkinter.Entry(self.top_frame, width = 10)
        

        self.score1_label.pack(side = 'left')
        self.score1_entry.pack(side = 'left')
        self.score2_label.pack(side = 'left')
        self.score2_entry.pack(side = 'left')
        self.score3_label.pack(side = 'left')
        self.score3_entry.pack(side = 'left')

        self.avg_button = tkinter.Button(self.main_window,text = 'Average', command=self.convert)              
        self.quit_button = tkinter.Button(self.main_window, text = 'Quit', command = self.main_window.destroy)

        self.avg_button.pack(side='left')
        self.quit_button.pack(side='right')

        tkinter.mainloop()

    def convert(self):
        avg = (float(self.score1_entry.get()) + float(self.score2_entry.get()) + float(self.score3_entry.get()))/3
        self.average_label.set(avg)
my_gui = average_grade()
