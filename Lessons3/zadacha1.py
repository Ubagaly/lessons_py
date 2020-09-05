try:
    def my_del(a, b):
        return a / b

    a = float(input("Введите число:"))
    b = float(input("Введите число:"))
    print(my_del(a, b))

except ZeroDivisionError as error:
    print("Ошибка: деление на ноль!!! Введите другое значение b")

