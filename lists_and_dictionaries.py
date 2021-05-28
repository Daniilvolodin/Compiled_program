import ctypes
import random
from tkinter import *

def list_clear(x, y, z):
    for list_1 in [x, y, z]:
        list_1.clear()


def check_operator(x):
    if x >= 0:
        return "+" + str(x)

    else:
        return str(x)


def remove_one(x):
    if x == 1:
        x = ''
        return x
    else:
        return x


# Adjusts screen to be 600 by 500
# and align it in the middle.
def set_size(x):
    # Grabs user screen aspects (resolution)
    height = int((ctypes.windll.user32.GetSystemMetrics(0) / 2) - 300)
    width = int(ctypes.windll.user32.GetSystemMetrics(1) / 2 - 250)
    x.state('normal')
    return x.geometry("600x500+{}+{}".format(height, width))

scale = 1
font_scale = 1

transparent = '#787878'

label_config = {
    'bg': '#787878',
    'font': 'helvetica 25 bold',
    'fg': 'white'

}

label_config_2 = {
    'bg': '#787878',
    'font': 'helvetica 13 bold',
    'fg': 'white'

}

button_config = {
    'bg': 'green',
    'fg': 'white',
    'relief': 'flat',
    'font': ('helvetica', 12 * scale, 'bold'),
    'activebackground': '#004d05',
    'activeforeground': 'white'
}

settings_label = {'bg': transparent,
                  'fg': 'white',
                  'font': 'Helvetica 25 underline'}

timer_buttons = {
    'font': 'Helvetica 10',
    'relief': 'flat'
}

two_point_q_label = {
    'bg': transparent,
    'fg': 'white'
}

entry_two_point_q = {
    'font': 'Helvetica 12',
    'justify': 'center'
}

q3_text = {
    'font': 'Helvetica 12 bold',
    'bg': transparent,
    'fg': 'white'

}

q3_entry = {
    'font': 'Helvetica 12',
    'justify': 'center',
    'relief': 'flat',
    'highlightthickness': 1,
    'highlightbackground': 'black',
    'highlightcolor': '#cccccc'

}

q3_button = {
    'relief': 'flat',
    'font': 'helvetica 12 bold'
}

back_button = {
    'text': 'Back',
    'bg': 'green',
    'fg': 'white',
    'relief': 'flat',
    'font': ('helvetica', 12 * scale, 'bold'),
    'activebackground': '#004d05',
    'activeforeground': 'white'

}

set_2_red = {
    'highlightbackground': 'red',
    'highlightcolor': 'red'
}

set_2_norm = {
    'highlightbackground': 'black',
    'highlightcolor': '#cccccc'
}

warning_labels = {
    'font': 'helvetica 13 bold',
    'fg': '#f78981',
    'text': '',
    'bg': transparent
}

next_button_design = {
    'relief': 'flat',
    'font': 'helvetica 10 bold'
}

timer_design = {
    'font': 'helvetica 16 underline',
    'fg': 'white',
    'bg': transparent

}

radio_button_design = {
    'font': 'helvetica 18 bold',
    'bg': 'white',
    'activebackground': 'black',
    'activeforeground': 'white',
    'fg': 'black',

}

correct = []

incorrect = []

typed_answers = []

correct_answers = []

randomized_question_gen = []

seconds_left = 30

minutes_left = 15

original_min = minutes_left
original_sec = seconds_left


class RandomizeAll:
    def __init__(self):
        self.acceptable = [random.randrange(-9, -1), random.randrange(1, 9)]


class timerCount:
    def __init__(self):
        self.minutes = minutes_left
        self.seconds = seconds_left
        self.timer = Label(text='Time remaining: %d:%d' % (minutes_left, seconds_left), **timer_design)
        self.timer.place(relx=0.5, rely=0.95, anchor=CENTER)
        self.timer.after(10, lambda: self.update_time())

    def update_time(self):
        self.seconds -= 1
        if self.seconds < 0:
            self.minutes -= 1
            self.seconds = 59
        seconds_left = self.seconds
        minutes_left = self.minutes
        self.timer.configure(text='Time remaining: %d:%d' % (minutes_left, seconds_left))
        self.timer.after(10, lambda: self.update_time())

