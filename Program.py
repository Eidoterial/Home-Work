import Function as Func
import Interface as In_f
import tkinter



class Program:

    def __init__(self):
        self.main_display = tkinter.Tk()
        self.main_display.geometry("800x600")
        self.main_display.configure(background="azure4")
        self.main_display.title("~Questeres~")


        self.buttons = In_f.Buttons(self.main_display, lambda : Func.start_test(self.variables, self.radio_b, self.buttons.backer, self.labels))

        self.variables = In_f.Variables()
        self.radio_b = In_f.RButon(self.main_display, self.variables)
        self.labels = In_f.Labeles(self.main_display)

        self.menu_if = In_f.MenuIF(self.main_display, lambda : Func.start_test(self.variables, self.radio_b, self.buttons.backer, self.labels), lambda : Func.show_score(self.variables, self.labels.quest_label), lambda :Func.save_file(self.variables, self.labels.quest_label))


    def run(self):
        self.main_display.mainloop()

program = Program()