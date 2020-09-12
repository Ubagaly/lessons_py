
with open("zadacha_1.txt", "w") as test_obj:
    test_f = input("Введите текст:")
    p = int(len(test_f))
    while p > 0:
        test_f = f"{test_f}\n"
        test_obj.write(test_f)
        test_f = input("Введите текст:")
        p = int(len(test_f))


with open("zadacha_1.txt", "r") as test_obj:
    for line in test_obj:
        print(line)

