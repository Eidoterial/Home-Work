today_year = 2024
today_month = 2

def check_user_name(name: str):

    if name.isalpha(): return True

    else: return False


def check_user_month(month: int):

    if 0 < month <= 12: return True

    else: return False


def check_user_year(year: int):

    if 0 < year <= 2024: return True

    else: return False


def test_born_date(month: int, year: int):

    tot_year = today_year - year
    tot_month = today_month - month

    if tot_month < 0:
        tot_month = 12 - abs(tot_month)
        tot_year -= 1

    elif tot_month == 0: tot_month = 1

    if 5 <= tot_year <= 119: return True

    else: return False
