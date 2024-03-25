import tkinter


class Variables:
    def __init__(self):
        self.score = 0 # Total score

        self.quest_correct = [tkinter.StringVar(value=None),
                                tkinter.StringVar(value=None),
                                tkinter.StringVar(value=None),
                                tkinter.StringVar(value=None),
                                tkinter.StringVar(value=None),
                                tkinter.StringVar(value=None),
                                tkinter.StringVar(value=None)]

        self.infor = tkinter.StringVar(value="""Правила прості
        За кожну правельну відповідь дається 1 очко
        В загальному є 7 питань
        Можливість подивитися результат
        Можливість збереження результату в txt файл""")



class Buttons:
    def __init__(self, main_display, back_func):
        self.backer = tkinter.Button(main_display, text="Далі", command=back_func)

class RButon:
    def __init__(self, main_display, variab):


        self.mask =[tkinter.Radiobutton(main_display),
                        tkinter.Radiobutton(main_display),
                        tkinter.Radiobutton(main_display),
                        tkinter.Radiobutton(main_display)]

        self.mask[0].config()

        self.quest = [[tkinter.Radiobutton(main_display, text="3", variable=variab.quest_correct[0], value="Uncorrect1"),
                        tkinter.Radiobutton(main_display, text="22", variable=variab.quest_correct[0], value="Uncorrect2"),
                        tkinter.Radiobutton(main_display, text="Риба", variable=variab.quest_correct[0], value="Uncorrect3"),
                        tkinter.Radiobutton(main_display, text="4", variable=variab.quest_correct[0], value="Correct")],

                      [tkinter.Radiobutton(main_display, text="4", variable=variab.quest_correct[1], value="Correct"),
                        tkinter.Radiobutton(main_display, text="В квадрату немає сторін", variable=variab.quest_correct[1], value="Uncorrect1"),
                        tkinter.Radiobutton(main_display, text="6", variable=variab.quest_correct[1], value="Uncorrect2"),
                        tkinter.Radiobutton(main_display, text="8", variable=variab.quest_correct[1], value="Uncorrect3")],

                      [tkinter.Radiobutton(main_display, text="Тому що ми хочемо митися", variable=variab.quest_correct[2], value="Uncorrect1"),
                        tkinter.Radiobutton(main_display, text="Підстава від природи", variable=variab.quest_correct[2], value="Uncorrect2"),
                        tkinter.Radiobutton(main_display, text="Це механізм терморегуляції організму", variable=variab.quest_correct[2], value="Correct"),
                        tkinter.Radiobutton(main_display, text="Це механізм відеорегуляції організму", variable=variab.quest_correct[2], value="Uncorrect3")],

                      [tkinter.Radiobutton(main_display, text="3,1415926535", variable=variab.quest_correct[3], value="Correct"),
                        tkinter.Radiobutton(main_display, text="3,1415906535", variable=variab.quest_correct[3], value="Uncorrect1"),
                        tkinter.Radiobutton(main_display, text="3,1415936535", variable=variab.quest_correct[3], value="Uncorrect2"),
                        tkinter.Radiobutton(main_display, text="3,1415946535", variable=variab.quest_correct[3], value="Uncorrect3")],

                      [tkinter.Radiobutton(main_display, text="Існують літаючі дерева", variable=variab.quest_correct[4], value="Uncorrect1"),
                        tkinter.Radiobutton(main_display, text="Корм для собак роблять з котів", variable=variab.quest_correct[4], value="Uncorrect2"),
                        tkinter.Radiobutton(main_display, text="Деякі папугаї можуть каркати", variable=variab.quest_correct[4], value="Correct"),
                        tkinter.Radiobutton(main_display, text="Не всі коні єдинороги", variable=variab.quest_correct[4], value="Uncorrect3")],

                      [tkinter.Radiobutton(main_display, text="Ви народилися сьогодні", variable=variab.quest_correct[5], value="Uncorrect1"),
                        tkinter.Radiobutton(main_display, text="Ви народитеся завтра", variable=variab.quest_correct[5], value="Uncorrect2"),
                        tkinter.Radiobutton(main_display, text="Ви народилися стільки років тому, скільки вам років", variable=variab.quest_correct[5], value="Correct"),
                        tkinter.Radiobutton(main_display, text="Ви не народжувалися", variable=variab.quest_correct[5], value="Uncorrect3")],

                      [tkinter.Radiobutton(main_display, text="Так", variable=variab.quest_correct[6], value="Uncorrect1"),
                        tkinter.Radiobutton(main_display, text="Звісно", variable=variab.quest_correct[6], value="Uncorrect2"),
                        tkinter.Radiobutton(main_display, text="Однозначно", variable=variab.quest_correct[6], value="Uncorrect3"),
                        tkinter.Radiobutton(main_display, text="Де я?", variable=variab.quest_correct[6], value="Correct")]]

class Lister:
    def __init__(self):
        pass

class Entrys:
    def __init__(self):
        pass

class Texts:
    def __init__(self):
        pass

class Labeles:
    def __init__(self, main_display):
        self.mask_l = tkinter.Label(main_display)

        self.quest_label = [tkinter.Label(main_display, text="2 + 2"),
                            tkinter.Label(main_display, text="Скільки сторін у квадрату"),
                            tkinter.Label(main_display, text="Чому люди потіють"),
                            tkinter.Label(main_display, text="Виберіть правельне число ПІ"),
                            tkinter.Label(main_display, text="Оберіть правельне твердження"),
                            tkinter.Label(main_display, text="Виберіть правельну відповідь"),
                            tkinter.Label(main_display, text="Вам сподобалося?)))"),]

class SpinBox:
    def __init__(self):
        pass


class LabelFraims:
    def __init__(self):
        pass

class Frames:
    def __init__(self):
        pass



class MenuIF:

    def __init__(self, main_display, start_func, score_func, save_func):
        self.main_menu_bar = tkinter.Menu(main_display)

        self.starter = tkinter.Menu(self.main_menu_bar)
        self.start = tkinter.Menu(self.starter)
        self.starter.add_command(label="Почати тест", command=start_func)

        main_display.config(menu = self.main_menu_bar)
        self.main_menu_bar.add_cascade(label="Стартер",menu = self.starter)
        self.main_menu_bar.add_command(label="Результат", command=score_func)
        self.main_menu_bar.add_command(label="Зберегти результат", command=save_func)



