
operations = ""

def input_number(variabls_numeral, number):
    variabls_numeral.set(variabls_numeral.get() + number)

def operation(variabls_numeral, result_variable, operation_input):
    global operations

    if operations == "":
        result_variable.set(variabls_numeral.get())
        variabls_numeral.set("")
        operations = operation_input
        print(result_variable.get(), operations)

    else:
        if operation_input == "=":
            if operations == "+":
                result_variable.set(str(float(result_variable.get()) + float(variabls_numeral.get())))
            elif operations == "-":
                result_variable.set(str(float(result_variable.get()) - float(variabls_numeral.get())))
            elif operations == "*":
                result_variable.set(str(float(result_variable.get()) * float(variabls_numeral.get())))
            elif operations == "/":
                result_variable.set(str(float(result_variable.get()) / float(variabls_numeral.get())))
            elif operations == "R":
                result_variable.set(str(round(float(result_variable.get()))))

        variabls_numeral.set(result_variable.get())
        operations = ""