import tkinter


class Variables:

    def __init__(self):
        self.select_number_input = tkinter.StringVar()
        self.result_calculate = tkinter.StringVar(value="0")

class Buttons:
    def __init__(self, input_number_frame, func, var, input_operation_frame, var2, funct2):
        self.numbers_buttons = []
        self.operators = []
        self.numbers_buttons.append(tkinter.Button(input_number_frame, text=f"{1}", width=6, height=1, command=lambda :func(var, str(1))))
        self.numbers_buttons.append(
            tkinter.Button(input_number_frame, text=f"{2}", width=6, height=1, command=lambda: func(var, str(2))))
        self.numbers_buttons.append(
            tkinter.Button(input_number_frame, text=f"{3}", width=6, height=1, command=lambda: func(var, str(3))))
        self.numbers_buttons.append(
            tkinter.Button(input_number_frame, text=f"{4}", width=6, height=1, command=lambda: func(var, str(4))))
        self.numbers_buttons.append(
            tkinter.Button(input_number_frame, text=f"{5}", width=6, height=1, command=lambda: func(var, str(5))))
        self.numbers_buttons.append(
            tkinter.Button(input_number_frame, text=f"{6}", width=6, height=1, command=lambda: func(var, str(6))))
        self.numbers_buttons.append(
            tkinter.Button(input_number_frame, text=f"{7}", width=6, height=1, command=lambda: func(var, str(7))))
        self.numbers_buttons.append(
            tkinter.Button(input_number_frame, text=f"{8}", width=6, height=1, command=lambda: func(var, str(8))))
        self.numbers_buttons.append(
            tkinter.Button(input_number_frame, text=f"{9}", width=6, height=1, command=lambda: func(var, str(9))))
        self.numbers_buttons.append(
            tkinter.Button(input_number_frame, text=f"{0}", width=6, height=1,command=lambda: func(var, str(0))))

        self.operators.append(tkinter.Button(input_operation_frame, text="+", width=6, height=1,
                              command=lambda: funct2(var, var2, "+")))
        self.operators.append(tkinter.Button(input_operation_frame, text="-", width=6, height=1,
                              command=lambda: funct2(var, var2, "-")))
        self.operators.append(tkinter.Button(input_operation_frame, text="*", width=6, height=1,
                              command=lambda: funct2(var, var2, "*")))
        self.operators.append(tkinter.Button(input_operation_frame, text="/", width=6, height=1,
                              command=lambda: funct2(var, var2, "/")))
        self.operators.append(tkinter.Button(input_operation_frame, text="=", width=6, height=1,
                              command=lambda: funct2(var, var2, "=")))
        self.operators.append(tkinter.Button(input_operation_frame, text="R", width=6, height=1,
                                             command=lambda: funct2(var, var2, "R")))

class Entrys:
    def __init__(self, calculate_main_display_frame, select_number_input):
        self.display_calculate = tkinter.Entry(calculate_main_display_frame, width=10, font=(None, 30), textvariable=select_number_input)


class Labeles:
    def __init__(self, fraim_random_num_generate, fraim_user_input_number):
        pass

class Frames:
    def __init__(self, main_display):
        self.calculate_main_display_frame = tkinter.Frame(main_display, background="red")
        self.zone_input_calculate_frame = tkinter.Frame(main_display, background="blue")
        self.input_number_frame = tkinter.Frame(self.zone_input_calculate_frame, background="green")
        self.input_operation_frame = tkinter.Frame(self.zone_input_calculate_frame, background="cyan")
