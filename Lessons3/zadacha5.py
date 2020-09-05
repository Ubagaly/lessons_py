try:
    def my_sum(my_num):
        sum1 = 0
        sum2 = 0
        while True:
            my_func = input("Введите последовательность чисел через пробел:")
            my_num = my_func.split(" ")

            for el in my_num:
                if el != "q":
                    el = float(el)
                    sum1 = sum1 + el
                else:
                    return (sum1)
                    break

            sum2 = sum1 + sum2
        return (sum2)
    print(my_sum(""))

except ValueError as error:
    print("Ошибка: Не верно введены значения.Введите числа через пробел")

