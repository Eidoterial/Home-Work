import Writer_data
import Suport_func
import User_data
class Program:

    def __init__(self):

        self.file_data = "User_data_info.txt"
        self.user = User_data.UserData()

    def start_program(self):

        print("Реєстрація та ввід даних")
        Suport_func.sleep(1)
        Suport_func.clear()

    def user_input_data(self):

        while True:

            if self.user.get_user_input(): break

    def write_filer_data(self):

        Writer_data.write_data_on_file(self.file_data, self.user)




if __name__ == "__main__":

    prog_meneger = Program()

    prog_meneger.start_program()
    prog_meneger.user_input_data()
    prog_meneger.write_filer_data()
