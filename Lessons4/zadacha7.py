try:
    c = int(input("Задайте число от которого нужно найти факториал:"))
    factorial = 1
    q = "*" * 30
    if c != 0:
        def fact():
            for el in range(1, c + 1):
                yield el

        for el in fact():
            factorial = el * factorial
        print(q)
        print(f"Факториал {c} равен: {factorial}")

    else:
        print(f"Факториал нуля равен: {factorial}")

except ValueError as error:
    print("Ошибка: Не верно введено значение.Введите число")




