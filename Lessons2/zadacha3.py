#Решение к задачи 3:
month = int(input("Введите номер месяца:"))
#вар. list
vremena = ['зима', 'весна', 'лето', 'осень']

if month > 12:
    print("Ошибка, параметр месяца задан не верно!")
elif month <= 2 or month == 12:
    print(vremena[0])
elif month >= 3 and month <= 5:
    print(vremena[1])
elif month >= 6 and month <= 8:
    print(vremena[2])
else:print(vremena[3])
# вар. dict

vremena_dict = {1: "зима", 2: "зима", 3: "весна",
               4: "весна", 5: "весна", 6: "лето",
               7: "лето", 8: "лето", 9: "осень",
               10: "осень", 11: "осень", 12: "зима"}

print(vremena_dict.get(month))

