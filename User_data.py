import Suport_func
import Check_user_data as Chud

class UserData:

    def __init__(self):

        self.user_name = str
        self.user_month = int
        self.user_year = int

        self.corect_user_name = False
        self.corect_user_month = False
        self.corect_user_year = False


    def get_user_input(self):

        if not self.corect_user_name:

            while True:
                print("Впишіть своє ім'я")
                test_name = input("--- >")
                Suport_func.clear()
                if Chud.check_user_name(test_name): break

                else:
                    print("Ім'я введено некоректно")
                    Suport_func.sleep(1)
                    Suport_func.clear()

            self.user_name = test_name
            self.corect_user_name = True

        if not self.corect_user_month:

            while True:

                test_month = Suport_func.str_blocker("Впишіть ваш номер місяця народження",
                                                     "Приклад: 6; 3; 11",
                                                     "Дані вписані коректно",
                                                     True,
                                                     True )

                if Chud.check_user_month(test_month): break

                else:
                    print("Місяць введено некоректно")
                    Suport_func.sleep(1)
                    Suport_func.clear()

            self.user_month = test_month

        if not self.corect_user_year:

            while True:

                test_year = Suport_func.str_blocker("Впишіть ваш рік народження",
                                                     "Приклад: 2000; 1987; 2011",
                                                     "Дані вписані коректно",
                                                     True,
                                                     True)

                if Chud.check_user_year(test_year): break

                else:
                    print("Рік введено некоректно")
                    Suport_func.sleep(1)
                    Suport_func.clear()

            self.user_year = test_year


        if Chud.test_born_date(self.user_month, self.user_year):
            print("Дані зареєстровано")

            self.corect_user_month = True
            self.corect_user_year = True
            Suport_func.sleep(1)
            Suport_func.clear()

            return True

        else:

            print("Ви не входите в віковий діапазон")
            print("Спробуйте ще раз")

            Suport_func.sleep(1)
            Suport_func.clear()

            return False


