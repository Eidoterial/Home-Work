import time
import os

sleep = lambda x: time.sleep(x)
clear = lambda : os.system("cls")


def check_run_func(status: bool, func_run):
    if status: func_run()

def str_blocker(first_messenge: str = "",
                re_messenge: str = "",
                end_messenge: str = "",
                clear_massenge: bool = False,
                sleep_next_meseenge: bool = False,
                sleep_time: int = 1):


    print(first_messenge)
    check_run_func(sleep_next_meseenge, sleep(sleep_time))

    check_run_func(clear_massenge, clear())
    while True:

        print(re_messenge)
        num = input("---> ")

        print("Обробка")
        check_run_func(sleep_next_meseenge, sleep(sleep_time))

        check_run_func(clear_massenge, clear())

        if num.isdigit():
            print(end_messenge)
            check_run_func(sleep_next_meseenge, sleep(sleep_time))
            check_run_func(clear_massenge, clear())

            return int(num)
        else:
            print("Ви ввели неправельні данні")
            check_run_func(sleep_next_meseenge, sleep(sleep_time))
            check_run_func(clear_massenge, clear())