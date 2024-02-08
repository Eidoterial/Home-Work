import time
import os

sleep = lambda x: time.sleep(x)
clear = lambda : os.system("cls")


def check_run_func(status: bool, func_run):
    if status: func_run()

def str_blocker(first_messenge: str = "",
                re_messenge: str = "",
                end_messenge: str = "",):


    print(first_messenge)
    sleep(1.5)

    clear()
    while True:

        print(re_messenge)
        num = input("---> ")

        print("Обробка")
        sleep(1.5)

        clear()

        if num.isdigit():
            print(end_messenge)
            sleep(1.5)
            clear()

            return int(num)
        else:
            print("Ви ввели неправельні данні")
            sleep(1.5)
            clear()