from menu_btn_contents import *
from tkinter import *


class CompileProgram:

    def __init__(self, parameter):
        self.parameter = parameter

        StartContent(self.parameter)
if __name__ == "__main__":
    root = Tk()
    app = CompileProgram(root)
    root.title('Algebra Quiz')
    set_size(x=root)
    root.configure(bg='#787878')
    photo = PhotoImage(file='iconchip.png')
    root.iconphoto(False, photo)
    root.mainloop()
