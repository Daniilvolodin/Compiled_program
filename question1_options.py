from tkinter import *
from lists_and_dictionaries import *


class OptionPick:
    def __init__(self, parameter):
        self.start_frame = Frame()
        self.parameter = parameter
        self.start_frame.place(relx=0.5, rely=0.5, anchor=CENTER)

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

        self.operators = ['+', '-']

        self.a_op = remove_one(x=self.x1 * self.x2)
        self.b_op = check_operator(x=(self.x1 * self.ran2) + (self.x2 * self.ran1))
        self.c_op = check_operator(x=(self.ran1 * self.ran2))

        self.alt_b_value = check_operator(x=int(self.b_op) - (2 * (self.x2 * self.ran2)))

        self.correct = "%sx²%sx%s" % (self.a_op, self.b_op, self.c_op)

        self.incorrect_1 = "{}x²{}x{}".format(self.a_op, str(self.b_op).replace(str(self.b_op)[0],
                                              self.operators[self.operators.index(str(self.b_op)[0]) - 1]),
                                              self.c_op)
        self.incorrect_2 = "{}x²{}x{}".format(self.a_op, self.b_op, check_operator(x=self.ran1 + self.ran2))
        self.incorrect_3 = "{}x²{}x{}".format(self.a_op, self.alt_b_value, self.c_op)

        self.shuffle_questions = [self.correct, self.incorrect_1, self.incorrect_2, self.incorrect_3]
        random.shuffle(self.shuffle_questions)

        self.user_pick = IntVar()

        self.question_label = Label(self.start_frame, **label_config, text=self.question)
        self.question_label.grid(row=0)

        self.option_frame = Frame(self.start_frame)
        self.option_frame.grid(row=1)

        self.option_1 = Radiobutton(self.option_frame, variable=self.user_pick, value=1,
                                    text=self.shuffle_questions[0], command=lambda: self.activate_next())
        self.option_2 = Radiobutton(self.option_frame, variable=self.user_pick, value=2,
                                    text=self.shuffle_questions[1], command=lambda: self.activate_next())
        self.option_3 = Radiobutton(self.option_frame, variable=self.user_pick, value=3,
                                    text=self.shuffle_questions[2], command=lambda: self.activate_next())
        self.option_4 = Radiobutton(self.option_frame, variable=self.user_pick, value=4,
                                    text=self.shuffle_questions[3], command=lambda: self.activate_next())

        self.option_1.grid(row=0, sticky=NSEW)
        self.option_2.grid(row=1, sticky=NSEW)
        self.option_3.grid(row=2, sticky=NSEW)
        self.option_4.grid(row=3, sticky=NSEW)

        self.next_button = Button(text="Next", command=lambda: self.check_answer(), state=DISABLED)
        self.next_button.place(relx=0.95, rely=0.95, anchor=CENTER)

    def activate_next(self):
        self.next_button.configure(state=NORMAL)

    def check_answer(self):
        if self.user_pick.get() - 1 == self.shuffle_questions.index(self.correct):
            correct.append("Correct")

        else:
            incorrect.append("Incorrect")
            correct_answers.append(self.correct)
        typed_answers.append(self.question)

for num in range(3):
    randomized_question_gen.append(OptionPick)
