from tkinter import *
from lists_and_dictionaries import *


class MenuButton:
    def __init__(self):
        self.menu_frame = Frame()
        self.menu_frame.place(relx=0.025, rely=0.025)
        self.menu_button = Button(self.menu_frame, **button_config,
                                  text='Menu Button', command=lambda:self.to_menu_screen())
        self.menu_button.grid(row=0, ipady=10, ipadx=10)

    def to_menu_screen(self):
        self.menu_frame.destroy()
        MenuScreen()


class MenuScreen:
    def __init__(self):
        self.menu_s_frame = Frame()
        self.menu_s_frame.place(relx=0.5, rely=0.5)

        self.timer_btn = Button(self.menu_s_frame, **button_config, text='Time')
        self.timer_btn.grid(row=0)