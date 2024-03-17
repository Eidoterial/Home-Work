import tkinter


class Variables:
    def __init__(self):
        self.color_chenges = tkinter.StringVar(value="red")

        self.age_status_car_v = tkinter.StringVar()
        self.continent_produs_car_v = tkinter.StringVar()
        self.mark_car_v = tkinter.StringVar()
        self.type_motor_v = tkinter.StringVar()
        self.capacity_motor_v = tkinter.StringVar()

class Buttons:
    def __init__(self, result_car_fr, func):
        self.res = tkinter.Button(result_car_fr, text="Результат", command=func)

class RButon:
    def __init__(self, label_frames, variables):

        # Вік машини
        self.r_b_age_1 = tkinter.Radiobutton(label_frames.age_status_car, text="до 5", value="до 5",
                                             variable=variables.age_status_car_v, background="burlywood4")
        self.r_b_age_2 = tkinter.Radiobutton(label_frames.age_status_car, text="6-10", value="6-10",
                                             variable=variables.age_status_car_v, background="burlywood4")
        self.r_b_age_3 = tkinter.Radiobutton(label_frames.age_status_car, text="11-15", value="11-15",
                                             variable=variables.age_status_car_v, background="burlywood4")
        self.r_b_age_4 = tkinter.Radiobutton(label_frames.age_status_car, text="більше 15", value="більше 15",
                                             variable=variables.age_status_car_v, background="burlywood4")

        # Континент розробника
        self.r_b_contin_1 = tkinter.Radiobutton(label_frames.continent_produs_car, text="Західна Європа", value="Західна Європа",
                                             variable=variables.continent_produs_car_v, background="burlywood4")
        self.r_b_contin_2 = tkinter.Radiobutton(label_frames.continent_produs_car, text="Східна Європа", value="Східна Європа",
                                             variable=variables.continent_produs_car_v, background="burlywood4")
        self.r_b_contin_3 = tkinter.Radiobutton(label_frames.continent_produs_car, text="Азія", value="Азія",
                                             variable=variables.continent_produs_car_v, background="burlywood4")
        self.r_b_contin_4 = tkinter.Radiobutton(label_frames.continent_produs_car, text="Америка", value="Америка",
                                             variable=variables.continent_produs_car_v, background="burlywood4")

        # Марка машини
        self.r_b_mark_1 = tkinter.Radiobutton(label_frames.mark_car, text="BMV", value="BMV",
                                                variable=variables.mark_car_v, background="burlywood4")
        self.r_b_mark_2 = tkinter.Radiobutton(label_frames.mark_car, text="Toyota", value="Toyota",
                                                variable=variables.mark_car_v, background="burlywood4")
        self.r_b_mark_3 = tkinter.Radiobutton(label_frames.mark_car, text="Nisan", value="Nisan",
                                                variable=variables.mark_car_v, background="burlywood4")
        self.r_b_mark_4 = tkinter.Radiobutton(label_frames.mark_car, text="Audi", value="Audi",
                                                variable=variables.mark_car_v, background="burlywood4")

        # Тип двигуна
        self.r_b_type_mtr_1 = tkinter.Radiobutton(label_frames.type_motor, text="Дизель", value="Дизель",
                                              variable=variables.type_motor_v, background="burlywood4")
        self.r_b_type_mtr_2 = tkinter.Radiobutton(label_frames.type_motor, text="Бендзин", value="Бендзин",
                                              variable=variables.type_motor_v, background="burlywood4")

        # Ємкість двигуна
        self.r_b_capas_mtr_1 = tkinter.Radiobutton(label_frames.capacity_motor, text="Менше 1200", value="Менше 1200",
                                              variable=variables.capacity_motor_v, background="burlywood4")
        self.r_b_capas_mtr_2 = tkinter.Radiobutton(label_frames.capacity_motor, text="1200-1500", value="1200-1500",
                                              variable=variables.capacity_motor_v, background="burlywood4")
        self.r_b_capas_mtr_3 = tkinter.Radiobutton(label_frames.capacity_motor, text="1501-2200", value="1501-2200",
                                              variable=variables.capacity_motor_v, background="burlywood4")
        self.r_b_capas_mtr_4 = tkinter.Radiobutton(label_frames.capacity_motor, text="Більше 2200", value="Більше 2200",
                                              variable=variables.capacity_motor_v, background="burlywood4")


class Lister:
    def __init__(self):
        pass

class Entrys:
    def __init__(self):
        pass

class Texts:
    def __init__(self, result_car_fr):
        self.result_show = tkinter.Text(result_car_fr)

class Labeles:
    def __init__(self):
        pass

class SpinBox:
    def __init__(self, car_info_selecter_fr, color_chenger, func):
        self.lister = ["red", "blue", "green", "yellow", "black"]
        self.color_spin = tkinter.Spinbox(car_info_selecter_fr, values=self.lister, textvariable=color_chenger, command=func, wrap=True)


class LabelFraims:
    def __init__(self, car_info_selecter_fr):
        self.status_car = tkinter.LabelFrame(car_info_selecter_fr, text="Виберіть бажаний статус машини", background="burlywood4")
        self.age_status_car = tkinter.LabelFrame(car_info_selecter_fr, text="Виберіть бажаний вік машини", background="burlywood4")
        self.continent_produs_car = tkinter.LabelFrame(car_info_selecter_fr, text="Континент виробника", background="burlywood4")

        self.mark_car = tkinter.LabelFrame(car_info_selecter_fr, text="Марка машини", background="burlywood4")
        self.type_motor = tkinter.LabelFrame(car_info_selecter_fr, text="Тип двигуна", background="burlywood4")

        self.capacity_motor = tkinter.LabelFrame(car_info_selecter_fr, text="Об'єм двигуна", background="burlywood4")

class Frames:
    def __init__(self, main_display, color_chenger):
        self.car_info_selecter_fr = tkinter.Frame(main_display, background="bisque4")
        self.result_car_fr = tkinter.Frame(main_display, background="burlywood3")

        self.colorest = tkinter.Frame(self.car_info_selecter_fr, background=color_chenger.get())
