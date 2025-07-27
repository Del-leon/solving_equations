def uravn_plus_and_minus(uravn_str):
    cash = ""
    coef_free = 0
    coef_x = 0
    last_operation = ""
    for i in uravn_str:
        if i == "x":
            if not(last_operation) or last_operation == "+":
                if not cash:
                    coef_x += 1
                else:
                    coef_x += int(cash)
            if last_operation == "-":
                if not cash:
                    coef_x -= 1
                else:
                    coef_x -= int(cash)
            cash = ""

        if i in "+-":
            if cash and last_operation:
                if last_operation == "+":
                    coef_free += int(cash)
                elif last_operation == "-":
                    coef_free -= int(cash)
            last_operation = i
            cash = ""

        if i in "0123456789":
            cash += i

    if cash:
        if last_operation == "+":
            coef_free += int(cash)
        elif last_operation == "-":
            coef_free -= int(cash)

    return coef_x, coef_free