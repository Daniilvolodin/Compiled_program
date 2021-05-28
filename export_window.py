from tkinter import *
from lists_and_dictionaries import *


class ResultsExport:
    def __init__(self, parameter):

        self.parameter = parameter

        self.start_frame = Frame(bg='black', padx=3, pady=3)
        self.start_frame.place(relx=0.5, rely=0.5, anchor=CENTER)

        self.content_frame = Frame(self.start_frame, bg='white')
        self.content_frame.grid(row=0)

        self.results_label = Label(self.content_frame, text='Results', font='helvetica 18 underline',
                                   justify=CENTER)
        self.results_label.grid(row=0, sticky=NSEW, pady=(0, 30))

        for x in range(len(typed_answers)):
            self.x = Label(self.content_frame, text=incorrect[x])
            self.x.grid(row=x+1, column=0)

            self.y = Label(self.content_frame, text=correct_answers[x])
            self.y.grid(row=x+1, column=1)

            self.z = Label(self.content_frame, text=typed_answers[x])
            self.z.grid(row=x+1, column=2)

