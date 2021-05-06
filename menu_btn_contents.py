from main_frame import *
from lists_and_dictionaries import *


class MenuButton:
    def __init__(self):
        self.menu_frame = Frame()
        self.menu_frame.place(relx=0.025, rely=0.025)
        self.menu_button = Button(self.menu_frame, **button_config,
                                  text='Menu Button')
        self.menu_button.grid(row=0, ipady=10, ipadx=10)


