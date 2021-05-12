from tkinter import *
from lists_and_dictionaries import *
from tkinter import ttk


class StartContent:
    def __init__(self):
        self.menu_frame = Frame()
        self.menu_frame.place(relx=0.025, rely=0.025)
        self.menu_button = Button(self.menu_frame, **button_config,
                                  text='Menu Button', command=lambda: self.to_menu_screen())
        self.menu_button.grid(row=0, ipady=10 * scale, ipadx=10 * scale)

        self.alg_quiz_frame = Frame(bg=transparent)
        self.alg_quiz_frame.place(relx=0.5, rely=0.5, anchor=CENTER)

        self.alg_quiz_label = Label(self.alg_quiz_frame, text='Algebra Quiz', **label_config)
        self.alg_quiz_label.grid(row=0, pady=(0, 15 * scale))

        self.alg_quiz_button = Button(self.alg_quiz_frame, text='Start Quiz', **button_config)
        self.alg_quiz_button.grid(row=1, ipadx=20 * scale, ipady=5 * scale)

    def to_menu_screen(self):
        self.menu_frame.destroy()
        self.alg_quiz_frame.destroy()
        MenuScreen()


class MenuScreen:
    def __init__(self):
        self.menu_s_frame = Frame(bg=transparent)
        self.menu_s_frame.place(relx=0.5, rely=0.25, anchor=CENTER)

        self.menu_content_frame = Frame(self.menu_s_frame, bg=transparent)
        self.menu_content_frame.grid(row=0)

        self.value_windowed = IntVar()

        self.menu_label = Label(self.menu_content_frame, text='Menu', **settings_label)
        self.menu_label.grid(row=0, sticky=NSEW)

        self.style = ttk.Style()
        self.change_res_slide = ttk.Checkbutton(self.menu_content_frame, text='Full Screen')
        self.style.configure('TCheckbutton', background=transparent, foreground='white',
                             font='helvetica 12 bold')
        self.change_res_slide.grid(row=1, sticky=NSEW)
        self.with_title_bar = ttk.Radiobutton(self.menu_content_frame, text='With Title Bar',
                                              value=0, variable=self.value_windowed)

        self.with_title_bar.grid(row=2, sticky=NSEW)

        self.without_title_bar = ttk.Radiobutton(self.menu_content_frame, text='Without Title Bar',
                                                 value=1, variable=self.value_windowed)
        self.style.configure('TRadiobutton', background=transparent, foreground='white',
                             font='helvetica 12 bold')
        self.without_title_bar.grid(row=3, sticky=NSEW)

        self.set_timer_btn = Button(self.menu_content_frame, text='Set Timer',
                                    bg='white', fg='black', command=lambda: self.to_timer())

        self.set_timer_btn.grid(row=4, sticky=NSEW, pady=10)

        self.apply_settings = Button(self.menu_content_frame, text='Apply Settings')
        self.apply_settings.grid(row=5, sticky=NSEW)

        self.b_b_frame = Frame()
        self.b_b_frame.place(relx=0.025, rely=0.025)
        self.back_btn = Button(self.b_b_frame, **button_config, text='Back',
                               command=lambda: self.back_menu())
        self.back_btn.grid(row=0, ipady=12 * scale, ipadx=12 * scale)

    def back_menu(self):
        for x in [self.menu_s_frame, self.b_b_frame]:
            x.destroy()
        StartContent()

    def to_timer(self):
        for x in [self.menu_s_frame, self.b_b_frame]:
            x.destroy()
        setTimer()


class setTimer:
    def __init__(self):

        self.starter_frame = Frame(bg=transparent)
        self.starter_frame.place(relx=0.5, rely=0.25, anchor=CENTER)

        self.timer_label = Label(self.starter_frame, text='Set Time', **settings_label)
        self.timer_label.grid(row=0)
