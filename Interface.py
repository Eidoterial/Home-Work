import tkinter



class Buttons:
    def __init__(self, fraim_random_num_generate, fraim_user_input_number):
        self.generate_random_num = tkinter.Button(fraim_random_num_generate, text="GENERATE", font=(None, 8), relief="flat")

        self.try_user_num = tkinter.Button(fraim_user_input_number, text="TRY", font=(None, 15), relief="flat")
        self.restart_game = tkinter.Button(fraim_user_input_number, text="RESTART", font=(None, 10), relief="flat")
        self.exit_game = tkinter.Button(fraim_user_input_number, text="EXIT", font=(None, 10), relief="flat")

class Entrys:
    def __init__(self, fraim_random_num_generate, fraim_user_input_number):
        self.entry_min_num = tkinter.Entry(fraim_random_num_generate, width=10)
        self.entry_max_num = tkinter.Entry(fraim_random_num_generate, width=10)

        self.entry_user_num = tkinter.Entry(fraim_user_input_number, width=30, font=(None, 20))


class Labeles:
    def __init__(self, fraim_random_num_generate, fraim_user_input_number):
        self.text_info_min = tkinter.Label(fraim_random_num_generate, text="Min number-->", font=(None, 8), relief="sunken", background="red")
        self.text_info_max = tkinter.Label(fraim_random_num_generate, text="<--Max number", font=(None, 8), relief="sunken", background="red")

        self.status_info_game = tkinter.StringVar(fraim_user_input_number, value="Введіть мінімальне та максимальне число")
        self.raunds = tkinter.StringVar(fraim_user_input_number, value="Raund: 0")

        self.text_info_game = tkinter.Label(fraim_user_input_number, textvariable=self.status_info_game, font=(None, 10), background="green", relief="groove")
        self.text_info_raund = tkinter.Label(fraim_user_input_number, textvariable=self.raunds, font=(None, 10), background="green", relief="groove")

class Frames:
    def __init__(self, main_display):
        self.fraim_random_num_generate = tkinter.Frame(main_display, width=400, height=50, background="red")
        self.fraim_user_input_number = tkinter.Frame(main_display, width=500, height=300, background="blue")
