with open("zadacha_5.txt", "w") as test_obj:
    test_f = input("Введите числа разделенные пробелами:")
    num_list = test_f.split(" ")
    print(num_list)
    test_obj.writelines(num_list)

with open("zadacha_5.txt", "r") as test_obj:
    sum_line = 0
    for line in test_obj:
        for el in line:
            el = int(el)
            sum_line = sum_line + el
        print(sum_line)