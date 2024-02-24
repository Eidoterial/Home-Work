from random import randint
import Interface as In_f
import tkinter

def generate_random_number():
    if program.entrys.entry_min_num.get().isdigit() and program.entrys.entry_max_num.get().isdigit():
        if int(program.entrys.entry_min_num.get()) <= int(program.entrys.entry_max_num.get()):
            program.random_num = randint(int(program.entrys.entry_min_num.get()), int(program.entrys.entry_max_num.get()))
            program.entrys.entry_min_num.delete(0, "end")
            program.entrys.entry_max_num.delete(0, "end")
            program.entrys.entry_min_num["state"] = "disabled"
            program.entrys.entry_max_num["state"] = "disabled"
            program.buttons.generate_random_num["state"] = "disabled"
            program.entrys.entry_user_num["state"] = "normal"
            program.buttons.try_user_num["state"] = "normal"
            program.buttons.restart_game["state"] = "normal"
            program.labeles.raunds.set(f"Raund: {program.now_round}")
            program.labeles.status_info_game.set("Вгадайте число")

        else:
            program.labeles.status_info_game.set("Завелике мінімальне число")
            program.entrys.entry_min_num.delete(0, "end")
            program.entrys.entry_max_num.delete(0, "end")
    else:
        program.labeles.status_info_game.set("Ви маєте ввести цілі числа")
        program.entrys.entry_min_num.delete(0, "end")
        program.entrys.entry_max_num.delete(0, "end")

def check_user_num():

    if program.now_round < program.round:

        if program.entrys.entry_user_num.get().isdigit():
            if int(program.entrys.entry_user_num.get()) == program.random_num:
                program.entrys.entry_user_num.delete(0, "end")
                program.labeles.status_info_game.set("Ви виграли")
                program.entrys.entry_user_num["state"] = "disabled"
                program.buttons.try_user_num["state"] = "disabled"
            elif int(program.entrys.entry_user_num.get()) < program.random_num:
                program.entrys.entry_user_num.delete(0, "end")
                program.labeles.status_info_game.set("Число замале")
                program.now_round += 1
            elif int(program.entrys.entry_user_num.get()) > program.random_num:
                program.entrys.entry_user_num.delete(0, "end")
                program.labeles.status_info_game.set("Число завелике")
                program.now_round += 1
            program.labeles.raunds.set(f"Raund: {program.now_round}")
        else:
            program.entrys.entry_user_num.delete(0, "end")
            program.labeles.status_info_game.set("Ви маєте ввести цілe число")
    else:
        program.entrys.entry_user_num.delete(0, "end")
        program.labeles.status_info_game.set("Ви програли")
        program.entrys.entry_user_num["state"] = "disabled"
        program.buttons.try_user_num["state"] = "disabled"

def restart_game():
    program.entrys.entry_user_num.delete(0, "end")
    program.labeles.status_info_game.set("Введіть мінімальне та максимальне число")
    program.entrys.entry_min_num["state"] = "normal"
    program.entrys.entry_max_num["state"] = "normal"
    program.buttons.generate_random_num["state"] = "normal"
    program.buttons.restart_game["state"] = "disabled"
    program.entrys.entry_user_num["state"] = "disabled"
    program.buttons.try_user_num["state"] = "disabled"
    program.labeles.raunds.set(f"Raund: 0")
    program.now_round = 1




def exits():
    program.main_display.quit()




class Program:

    def __init__(self):
        self.main_display = tkinter.Tk()
        self.main_display.geometry("600x450")

        self.fraims = In_f.Frames(self.main_display)
        self.labeles = In_f.Labeles(self.fraims.fraim_random_num_generate, self.fraims.fraim_user_input_number)
        self.entrys = In_f.Entrys(self.fraims.fraim_random_num_generate, self.fraims.fraim_user_input_number)
        self.buttons = In_f.Buttons(self.fraims.fraim_random_num_generate, self.fraims.fraim_user_input_number)

        self.round = 5
        self.now_round = 1

        self.random_num = 0

        self.entrys.entry_user_num["state"] = "disabled"
        self.buttons.try_user_num["state"] = "disabled"
        self.buttons.restart_game["state"] = "disabled"


        self.buttons.generate_random_num["command"] = generate_random_number
        self.buttons.try_user_num["command"] = check_user_num
        self.buttons.exit_game["command"] = exits
        self.buttons.restart_game["command"] = restart_game

        self.main_display.wm_title(f"Game_prototype 1.0")
        self.main_display.config(background="green")


    def run(self):
        self.fraims.fraim_random_num_generate.place(relx=0.2, rely=0.1, relwidth=0.6, relheight=0.1)
        self.labeles.text_info_min.place(relx=0.02, rely=0.35, relwidth=0.21, relheight=0.3)
        self.labeles.text_info_max.place(relx=0.77, rely=0.35, relwidth=0.21, relheight=0.3)
        self.entrys.entry_min_num.place(relx=0.24, rely=0.35, relwidth=0.15, relheight=0.3)
        self.entrys.entry_max_num.place(relx=0.61, rely=0.35, relwidth=0.15, relheight=0.3)
        self.buttons.generate_random_num.place(relx=0.4, rely=0.35, relwidth=0.2, relheight=0.3)


        self.fraims.fraim_user_input_number.place(relx=0.1, rely=0.2, relwidth=0.8, relheight=0.6)
        self.buttons.try_user_num.place(relx=0.3, rely=0.85, relwidth=0.4, relheight=0.1)
        self.buttons.restart_game.place(relx=0.05, rely=0.85, relwidth=0.15, relheight=0.1)
        self.buttons.exit_game.place(relx=0.8, rely=0.85, relwidth=0.15, relheight=0.1)
        self.entrys.entry_user_num.place(relx=0.35, rely=0.7, relwidth=0.3, relheight=0.1)
        self.labeles.text_info_game.place(relx=0.2, rely=0.3, relwidth=0.6, relheight=0.1)
        self.labeles.text_info_raund.place(relx=0.02, rely=0.1, relwidth=0.2, relheight=0.1)

        self.main_display.mainloop()

program = Program()