import Function as Func
import Interface as In_f
import tkinter


def exits():
    program.main_display.quit()




class Program:

    def __init__(self):
        self.main_display = tkinter.Tk()
        self.main_display.geometry("400x450")

        self.variables = In_f.Variables()

        self.functions1 = Func.input_number
        self.functions2 = Func.operation

        self.frames = In_f.Frames(self.main_display)

        self.buttons = In_f.Buttons(self.frames.input_number_frame, self.functions1, self.variables.select_number_input, self.frames.input_operation_frame, self.variables.result_calculate, self.functions2)

        self.entrys = In_f.Entrys(self.frames.calculate_main_display_frame, self.variables.select_number_input)


    def run(self):
        self.frames.calculate_main_display_frame.place(relx=0, rely=0, relwidth=1, relheight=0.2)
        self.entrys.display_calculate.place(relx=0.05, rely=0.05, relwidth=0.9, relheight=0.9)


        self.frames.zone_input_calculate_frame.place(relx=0, rely=0.2, relwidth=1, relheight=0.8)
        self.frames.input_number_frame.place(relx=0.05, rely=0.1, relwidth=0.55, relheight=0.8)

        ibnl = 0
        for r in range(3):
            for c in range(3):
                self.buttons.numbers_buttons[ibnl].grid(row=r, column=c, padx=10, pady=23)
                ibnl += 1

        self.buttons.numbers_buttons[ibnl].grid(row=4, column=1, padx=10, pady=23)


        self.frames.input_operation_frame.place(relx=0.65, rely=0.1, relwidth=0.3, relheight=0.8)

        ibnl = 0
        for r in range(2):
            for c in range(2):
                self.buttons.operators[ibnl].grid(row=r, column=c, padx=5, pady=25)
                ibnl += 1

        self.buttons.operators[ibnl].grid(row=3, column=0, padx=5, pady=23)
        self.buttons.operators[ibnl + 1].grid(row=3, column=1, padx=5, pady=23)

        self.main_display.mainloop()

program = Program()