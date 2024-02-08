

def write_data_on_file(file_name: str, data: object):

    with open(file_name, "a", encoding="utf-8") as d_f:

        d_f.write(f"Ім'я: {data.user_name} \n")
        d_f.write(f"Місяць: {str(data.user_month)} \n")
        d_f.write(f"Рік народженя: {(data.user_year)} \n")
