import ctypes
import random


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

back_button = {
    'text': 'Back',
    'bg': 'green',
    'fg': 'white',
    'relief': 'flat',
    'font': ('helvetica', 12 * scale, 'bold'),
    'activebackground': '#004d05',
    'activeforeground': 'white'

}

# Two entries per question
already_answered_root = []

# Four options per question (Four vari)
already_answered_opt = []

# Three Entries per question (two roots and one simplified expression)
already_answered_two = []

correct = []

incorrect = []

typed_answers = []

correct_answers = []

seconds_left = 30

minutes_left = 15


class RandomizeAll:
    def __init__(self):
        self.acceptable = [random.randrange(-9, -1), random.randrange(1, 9)]