from tkinter import *
from menu_btn_contents import *
from lists_and_dictionaries import *


class CompileProgram:

    def __init__(self, parameter):
        MenuButton()
        self.parameter = parameter


root = Tk()
app = CompileProgram(root)
root.title('Algebra Quiz')
root.geometry('800x650')
root.configure(bg='#787878')
photo = PhotoImage(file='iconchip.png')
root.iconphoto(False, photo)
root.mainloop()
