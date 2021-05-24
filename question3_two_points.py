from tkinter import *
from lists_and_dictionaries import *


class TwoPointQ:
    def __init__(self, parameter):

        self.parameter = parameter

        self.random_num_1 = random.choice(RandomizeAll().acceptable)
        self.random_num_2 = random.choice(RandomizeAll().acceptable)

        self.b_value = check_operator(x=(self.random_num_1 + self.random_num_2))
        self.c_value = check_operator(x=(self.random_num_1 * self.random_num_2))
        self.question_gen = "x²%sx%s" % (self.b_value, self.c_value)

        self.question_prob = 'The area of a rectangle\n' \
                             'can be represented by: %s.\n ' \
                             'Find simplified quadratic form\n and define its roots' % self.question_gen

        self.start_frame = Frame(bg=transparent)
        self.start_frame.place(relx=0.5, rely=0.3, anchor=CENTER)

        self.question_label = Label(self.start_frame, text=self.question_prob, **two_point_q_label,
                                    font='Helvetica 12 bold', wrap=240)
        self.question_label.grid(row=0)

        self.contents_frame = Frame(self.start_frame, bg=transparent)
        self.contents_frame.grid(row=1, sticky=NSEW)

        self.simplified_ex_label = Label(self.contents_frame, text='Simplified expression:',
                                         **q3_text)
        self.simplified_ex_label.grid(row=0, column=0)

        self.simplified_ex_entry = Entry(self.contents_frame, **q3_entry)
        self.simplified_ex_entry.grid(row=0, column=1, ipady=3)

        self.root_1_label = Label(self.contents_frame, text='Root 1:',
                                  **q3_text)
        self.root_1_label.grid(row=1, column=0)

        self.root_1_entry = Entry(self.contents_frame, **q3_entry)
        self.root_1_entry.grid(row=1, column=1, ipady=3)

        self.root_2_label = Label(self.contents_frame, text='Root 2:', **q3_text)
        self.root_2_label.grid(row=2, column=0)

        self.root_2_entry = Entry(self.contents_frame, **q3_entry)
        self.root_2_entry.grid(row=2, column=1, ipady=3)

        self.buttons_frame = Frame(self.start_frame)
        self.buttons_frame.grid(row=2)

        self.b1 = Button(self.buttons_frame, text='Check')
        self.b1.grid(row=0, column=0, ipadx=10, ipady=3)

        self.b2 = Button(self.buttons_frame, text='?')
        self.b2.grid(row=0, column=1, ipadx=10, ipady=3)
