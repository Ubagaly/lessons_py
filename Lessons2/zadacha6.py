#Решение к задачи 6:
list_tovarov = []
name_list = []
price_list = []
volume_list = []
unit_list = []
dict_analis = {"наименование": name_list, "цена": price_list, "количество": volume_list,
               "ед.": unit_list}
name1 = input("Введите наименование товара:")
num = 1
poz = 0
while name1 != "":
    name_list.insert(poz, name1)
    price1 = input("Цена товара:")
    price_list.insert(poz, price1)
    volume1 = input("Введите количество товара:")
    volume_list.insert(poz, volume1)
    unit1 = input("Единица измерения товара:")
    unit_list.insert(poz, unit1)
    my_list = [["наименование", name1],
               ["цена", price1],
               ["количество", volume1],
               ["ед.", unit1]
               ]
    my_dict = dict(my_list)
    my_kartocka = (num, my_dict)
    list_tovarov.insert(poz, my_kartocka)
    num = num + 1
    poz = poz + 1
    name1 = input("Введите наименование товара:")

for el in list_tovarov:
    print(el)
print(dict_analis)





