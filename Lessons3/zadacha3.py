try:
    def my_func(a, b, c):
        if a <= b and a <= c:
            sum = b + c
        elif b <= a and b <= c:
            sum = a + c
        else:
            sum = a + b
        return sum


    a = float(input("Введите число:"))
    b = float(input("Введите число:"))
    c = float(input("Введите число:"))
    print(my_func(a, b, c))

except ValueError as error:
    print("Ошибка: Не верно введены значения.Введите числа")