import Function as Func
import Interface as In_f
import tkinter



class Program:

    def __init__(self):
        self.main_display = tkinter.Tk()
        self.main_display.geometry("400x450")
        self.main_display.title("Конвентор валют")



    def run(self):

        self.main_display.mainloop()

program = Program()