input_str = input("Введите уравнение: ").replace(" ", "")
print(f"Введенное уравнение: {input_str}")

coef_x_left = 0
coef_free_left = 0

next_side = False
last_operation = ""

coef_x_right = 0
coef_free_right = 0

cash = ""
for i in input_str:

    if i == "x":
        if next_side and (not(last_operation) or last_operation == "+"):
            if not cash:
                coef_x_right += 1
            else:
                coef_x_right += int(cash)

        elif next_side and last_operation == "-":
            if not cash:
                coef_x_right -= 1
            else:
                coef_x_right -= int(cash)

        elif not(next_side) and (not(last_operation) or last_operation == "+"):
            if not cash:
                coef_x_left += 1
            else:
                coef_x_left += int(cash)

        elif not(next_side) and last_operation == "-":
            if not cash:
                coef_x_left -= 1
            else:
                coef_x_left -= int(cash)

        cash = ""

    elif i in "+-":
        if cash:
            if next_side and last_operation:
                if last_operation == "+":
                    coef_free_right += int(cash)
                elif last_operation == "-":
                    coef_free_right -= int(cash)
            elif last_operation:
                if last_operation == "+":
                    coef_free_left += int(cash)
                elif last_operation == "-":
                    coef_free_left -= int(cash)
        
        last_operation = i
        cash = ""

    elif i in "0123456789":
        cash += i
    
    elif i == "=":
        if last_operation == "+":
            coef_free_left += int(cash)
        elif last_operation == "-":
            coef_free_left -= int(cash)

        next_side = True
        cash = ""
        last_operation = ""

if cash:
    if last_operation == "+":
        coef_free_right += int(cash)
    elif last_operation == "-":
        coef_free_right -= int(cash)

print(coef_x_left, coef_free_left)
print(coef_x_right, coef_free_right)
# plus and minus