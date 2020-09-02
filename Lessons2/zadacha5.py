#Решение к задачи 5:
my_spicok = [5, 7, 9, 3, 2, 6, 3, 23]
my_spicok.sort()

print(my_spicok)
a = int(input("Введите элемент списка:"))
num=0


for el in my_spicok:
    if a >= my_spicok[-1]:
        my_spicok.append(a)
        my_spicok.reverse()
        print(my_spicok)
        break
    elif my_spicok[num] >= a:
        my_spicok.insert(num, a)
        my_spicok.reverse()
        print(my_spicok)
        break

    else: num = num + 1






