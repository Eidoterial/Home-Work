import Function as Func
import Interface as In_f
import tkinter



class Program:

    def __init__(self):
        self.main_display = tkinter.Tk()
        self.main_display.geometry("800x700")
        self.main_display.configure(background="azure4")
        self.main_display.title("Car")

        self.variables = In_f.Variables()

        self.frames = In_f.Frames(self.main_display, self.variables.color_chenges)
        self.label_frames = In_f.LabelFraims(self.frames.car_info_selecter_fr)
        self.texts = In_f.Texts(self.frames.result_car_fr)
        self.butt = In_f.Buttons(self.frames.result_car_fr, lambda : Func.show(self.variables, self.texts.result_show))


        self.spin_boxes = In_f.SpinBox(self.frames.car_info_selecter_fr, self.variables.color_chenges,
                                       lambda : Func.changes_color(self.variables.color_chenges.get(), self.frames.colorest))

        self.r_button = In_f.RButon(self.label_frames, self.variables)


    def run(self):

        # Фрейм вибору машини ##########################################################################################
        self.frames.car_info_selecter_fr.place(relx=0.05, rely = 0.05, relwidth=0.9, relheight= 0.6)

        # Ліва частина -------------------------------------------------------------------------------------------------
        self.label_frames.status_car.place(relx=0.05, rely = 0.05, relwidth=0.3, relheight= 0.2)

        # Встановлення віку
        self.label_frames.age_status_car.place(relx=0.05, rely = 0.3, relwidth=0.3, relheight= 0.3)
        self.r_button.r_b_age_1.place(relx=0.05, rely = 0.1)
        self.r_button.r_b_age_2.place(relx=0.05, rely = 0.3)
        self.r_button.r_b_age_3.place(relx=0.05, rely = 0.5)
        self.r_button.r_b_age_4.place(relx=0.05, rely = 0.7)

        # Встановлення континенту 
        self.label_frames.continent_produs_car.place(relx=0.05, rely = 0.7, relwidth=0.3, relheight= 0.25)
        self.r_button.r_b_contin_1.place(relx=0.05, rely=0.1)
        self.r_button.r_b_contin_2.place(relx=0.05, rely=0.3)
        self.r_button.r_b_contin_3.place(relx=0.05, rely=0.5)
        self.r_button.r_b_contin_4.place(relx=0.05, rely=0.7)

        # Середня частина ----------------------------------------------------------------------------------------------

        # Встановлення марки
        self.label_frames.mark_car.place(relx=0.45, rely=0.3, relwidth=0.2, relheight=0.4)
        self.label_frames.continent_produs_car.place(relx=0.05, rely=0.7, relwidth=0.3, relheight=0.25)
        self.r_button.r_b_mark_1.place(relx=0.05, rely=0.1)
        self.r_button.r_b_mark_2.place(relx=0.05, rely=0.3)
        self.r_button.r_b_mark_3.place(relx=0.05, rely=0.5)
        self.r_button.r_b_mark_4.place(relx=0.05, rely=0.7)

        # Встановлення типу двигуна
        self.label_frames.type_motor.place(relx=0.45, rely=0.75, relwidth=0.2, relheight=0.2)
        self.r_button.r_b_type_mtr_1.place(relx=0.05, rely=0.1)
        self.r_button.r_b_type_mtr_2.place(relx=0.05, rely=0.4)




        # Права частина ------------------------------------------------------------------------------------------------

        # Встановлення ємкості двигуна
        self.label_frames.capacity_motor.place(relx=0.75, rely=0.3, relwidth=0.2, relheight=0.4)
        self.r_button.r_b_capas_mtr_1.place(relx=0.05, rely=0.1)
        self.r_button.r_b_capas_mtr_2.place(relx=0.05, rely=0.3)
        self.r_button.r_b_capas_mtr_3.place(relx=0.05, rely=0.5)
        self.r_button.r_b_capas_mtr_4.place(relx=0.05, rely=0.7)
        self.spin_boxes.color_spin.place(relx=0.75, rely=0.75, relwidth=0.2, relheight=0.05)
        self.frames.colorest.place(relx=0.75, rely=0.85, relwidth=0.2, relheight=0.1)

        # Фрейм виводу результату ######################################################################################
        self.frames.result_car_fr.place(relx=0.05, rely=0.7, relwidth=0.9, relheight= 0.3 )
        self.texts.result_show.place(relx=0.05, rely=0.1, relwidth=0.9, relheight= 0.4)
        self.butt.res.place(relx=0.4, rely=0.5, relwidth=0.2, relheight= 0.1)



        self.main_display.mainloop()

program = Program()