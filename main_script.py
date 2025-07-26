import Operations

input_str = input("Введите уравнение: ").replace(" ", "")
print(f"Уравнение: {input_str}")

input_str = input_str.split("=")
uravn_left = input_str[0]
print(uravn_left)
uravn_right = input_str[1]
print(uravn_right)

coef_x_left, coef_free_left = Operations.uravn_plus_and_minus(uravn_left)

coef_x_right, coef_free_right = Operations.uravn_plus_and_minus(uravn_right)

print(coef_x_left, coef_free_left)
print(coef_x_right, coef_free_right)
# plus and minus