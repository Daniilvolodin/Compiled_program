# Icon source: https://www.cleanpng.com/png-question-mark-png-41220/

from tkinter import *
from lists_and_dictionaries import *
from functools import partial


def value_error(x):
    try:
        float(x.get())
    except ValueError:
        x.configure(highlightbackground='red', highlightcolor='red')
    else:
        x.configure(highlightbackground='black', highlightcolor='#cccccc')
        pass


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
        self.start_frame.place(relx=0.5, rely=0.4, anchor=CENTER)

        self.question_label = Label(self.start_frame, text=self.question_prob, **two_point_q_label,
                                    font='Helvetica 12 bold', wrap=240)
        self.question_label.grid(row=0)

        self.contents_frame = Frame(self.start_frame, bg=transparent)
        self.contents_frame.grid(row=1, sticky=NSEW, pady=(20, 0))

        self.simplified_ex_label = Label(self.contents_frame, text='Simplified expression:',
                                         **q3_text)
        self.simplified_ex_label.grid(row=0, column=0)

        self.simplified_ex_entry = Entry(self.contents_frame, **q3_entry)
        self.simplified_ex_entry.grid(row=0, column=1, ipady=3)

        self.root_1_label = Label(self.contents_frame, text='Root 1:',
                                  **q3_text)
        self.root_1_label.grid(row=1, column=0, pady=10)

        self.root_1_entry = Entry(self.contents_frame, **q3_entry)
        self.root_1_entry.grid(row=1, column=1, ipady=3)

        self.root_2_label = Label(self.contents_frame, text='Root 2:', **q3_text)
        self.root_2_label.grid(row=2, column=0)

        self.root_2_entry = Entry(self.contents_frame, **q3_entry)
        self.root_2_entry.grid(row=2, column=1, ipady=3)

        self.buttons_frame = Frame(self.start_frame, bg=transparent)
        self.buttons_frame.grid(row=2, pady=(10, 0))

        self.check = Button(self.buttons_frame, text='Check', font='helvetica 12 bold', relief=FLAT,
                            command=lambda: self.check_input())
        self.check.grid(row=0, column=0, ipadx=70, ipady=3)

        self.question = Button(self.buttons_frame, text='?', font='helvetica 12 bold', relief=FLAT,
                               command=lambda: self.open_help(self))
        self.question.grid(row=0, column=1, ipadx=10, ipady=3, padx=(10, 0))

        self.next_button = Button(text="Next", state=DISABLED)
        self.next_button.place(relx=0.95, rely=0.95, anchor=CENTER)

    def check_input(self):

        value_error(x=self.root_1_entry)
        value_error(x=self.root_2_entry)

        if not re.match(r'^\(x[+\-]\d*\)\(x[+\-]\d*\)$', self.simplified_ex_entry.get()):
            self.simplified_ex_entry.configure(highlightbackground='red', highlightcolor='red')
        else:
            self.simplified_ex_entry.configure(highlightbackground='black', highlightcolor='#cccccc')

            try:
                [float(x) for x in [self.root_1_entry.get()]]
            except ValueError:
                pass
            else:
                self.next_button.configure(state=NORMAL)

    def open_help(self, parameter):
        HelpWindow(parameter)
        self.question.configure(state=DISABLED)


class HelpWindow:
    def __init__(self, parameter):
        self.parameter = parameter

        self.new_window = Toplevel(bg=transparent)
        photo = PhotoImage(file='question_symbol.png')
        self.new_window.iconphoto(False, photo)
        self.new_window.title('Help')
        self.new_window.geometry('340x400')

        self.new_frame = Frame(self.new_window, bg=transparent)
        self.new_frame.place(relx=0.5, rely=0.5, anchor=CENTER)

        self.help_title = Label(self.new_frame, text='Help Index', bg=transparent,
                                font='Helvetica 20 bold', fg='white')
        self.help_title.grid(row=0)

        self.help_desc = Label(self.new_frame, text="Enter your answer in a form of "
                                                    "simplified quadratic equation\n\n"
                                                    "When using exemplars, change "
                                                    "hash tags to a number for "
                                                    "program to validate your input.", bg=transparent,
                               wrap=260, fg='white', font='helvetica 13 italic')
        self.help_desc.grid(row=1)

        self.button_frame = Frame(self.new_frame, bg=transparent)
        self.button_frame.grid(row=2, pady=(20, 0))

        self.set_exemplar = Button(self.button_frame, text='Set Exemplar', relief=FLAT)
        self.set_exemplar.grid(row=0, column=0, padx=(0, 10), ipady=3, ipadx=15)

        self.dismiss = Button(self.button_frame, text='Dismiss', relief=FLAT)
        self.dismiss.grid(row=0, column=1, ipady=3, ipadx=15)
