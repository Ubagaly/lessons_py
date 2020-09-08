try:
    def my_func(x, y):
        stepen1 = 1
        stepen2 = 1
        num = 1
        el = 1
        if y >= 0:
            return "Вы не верно задали значение y - число должно быть ОТРИЦАТЕЛЬНЫМ"
        else:
            stepen1 = x ** y

        while el <= abs(y):
            num = num * x
            stepen2 = 1 / num
            el = el + 1
        return stepen1, stepen2


    x = abs(float(input("Введите любое число:")))
    y = int(input("Введите целое отрицательно число:"))

    print(my_func(x, y))

except ValueError as error:
    print("Ошибка: Не верно введены значения.Введите числа")


