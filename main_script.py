input_str = input("Введите уравнение: ")
print(f"Уравнение: {input_str}")

coef_x_left = []
coef_free_left = []

coef_x_right = []
coef_free_right = []

cash = ""
for i in input_str:

    if i == "x":
        if not cash:
            coef_x_left.append(1)
        else:
            coef_x_left.append(int(cash))

        cash = ""

    elif i in "+-*/" and not cash:
        cash += i

    elif i in "0123456789":
        cash += i

print(coef_x_left, coef_free_left)
