def changes_color(new_color, color_fraim):
    color_fraim.configure(background=new_color)


def show(vars, text):
    text.insert(1.0, f"Колір - {vars.color_chenges.get()} ")
    text.insert(1.0, f"Об'єм - {vars.capacity_motor_v.get()} ")
    text.insert(1.0, f"Тип - {vars.type_motor_v.get()} ")
    text.insert(1.0, f"Марка - {vars.mark_car_v.get()} ")
    text.insert(1.0, f"Континент - {vars.continent_produs_car_v.get()} ")
    text.insert(1.0, f"Вік - {vars.age_status_car_v.get()} ")
