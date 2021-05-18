from tkinter import *
from lists_and_dictionaries import *


class OptionPick:
    def __init__(self):
        self.start_frame = Frame()
        self.start_frame.place(relx=0.5, rely=0.3, anchor=CENTER)

        self.button_frame = Frame()
        self.button_frame.grid()
        self.coefficient_pick = [1, 2, 3]

        self.x1 = random.choice(self.coefficient_pick)
        self.x2 = random.choice(self.coefficient_pick)

        self.ran1 = check_operator(x=random.choice(RandomizeAll().acceptable))
        self.ran2 = check_operator(x=random.choice(RandomizeAll().acceptable))

        self.question = "({}x{})({}x{})".format(remove_one(x=self.x1), self.ran1, remove_one(x=self.x2),
                                                self.ran2)

        self.ran1 = int(self.ran1)
        self.ran2 = int(self.ran2)

        self.correct = "%sx²%sx%s" % (
            remove_one(x=self.x1 * self.x2), check_operator(x=(self.x1 * self.ran2) + (self.x2 * self.ran1)),
            check_operator(x=(self.ran1 * self.ran2)))

        self.incorrect_1 = ''
        self.incorrect_2 = ''
        self.incorrect_3 = ''


        self.question_label = Label(self.start_frame, **label_config, text=self.question)
        self.question_label.grid(row=0)

        self.option_frame = Frame(self.start_frame)
        self.option_frame.grid(row=1, sticky=NSEW)

        self.option_1 = Radiobutton(self.option_frame)
        self.option_2 = Radiobutton(self.option_frame)
        self.option_3 = Radiobutton(self.option_frame)
        self.option_4 = Radiobutton(self.option_frame)

        self.option_1.grid(row=0)
        self.option_2.grid(row=1)
        self.option_3.grid(row=2)
        self.option_4.grid(row=3)

    def ran_all(self):
        pass
