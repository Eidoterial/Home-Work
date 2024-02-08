import Suport_func

class UserData:

    def __init__(self):

        self.user_name = str
        self.user_month = int
        self.user_year = int

        self.corect_user_name = False
        self.corect_user_month = False
        self.corect_user_year = False


    def get_user_input(self):

        test_user_month = int
        test_user_year = int

        if not self.corect_user_name:

            while True:
                print("Впишіть своє ім'я")
                test_user_name = input("--- >")



