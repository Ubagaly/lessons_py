#Создайте собственный класс-исключение, который должен проверять содержимое списка на наличие
# только чисел. Проверить работу исключения на реальном примере. Необходимо запрашивать у пользователя
# данные и заполнять список. Класс-исключение должен контролировать типы данных элементов списка.
#Примечание: длина списка не фиксирована. Элементы запрашиваются бесконечно, пока пользователь сам
# не остановит работу скрипта, введя, например, команду “stop”. При этом скрипт завершается,
# сформированный список выводится на экран.
class ValueError(Exception):
    def __init__(self, txt):
        self.txt = txt


num_list = []
num = input("Введите число:")
while num != "stop":
    try:
        if num.isdigit() == False:
            raise ValueError("Вы ввели не число")

        num_list.append(num)
        num = input("Введите число:")
    except ValueError as err:
        print(err)
        num = input("Введите число:")

else:
    print(f"Все хорошо. Ваш лист: {num_list}")




