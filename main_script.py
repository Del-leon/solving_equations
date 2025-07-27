from operations import uravn_plus_and_minus

input_str = input("Введите уравнение: ").replace(" ", "")
print(f"Уравнение: {input_str}")

input_str = input_str.split("=")
uravn_left, uravn_right = input_str
print(uravn_left)
print(uravn_right)

coef_x_left, coef_free_left = uravn_plus_and_minus(uravn_left)

coef_x_right, coef_free_right = uravn_plus_and_minus(uravn_right)

print(f"Сумма коэффициентов при х слева{coef_x_left}")
print(f"Сумма коэффициентов при х справа{coef_x_right}")
print(f"Сумма свободных коэффициентов слева{coef_free_left}")
print(f"Сумма свободных коэффициентов справа{coef_free_right}")
