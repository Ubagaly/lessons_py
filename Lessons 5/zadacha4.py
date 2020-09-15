with open("zadacha_4.txt", "r") as test_obj:
    for line in test_obj:
        num_list = line.split("—")

        if num_list[0] == "One":
            num_list[0] = "Один-"
            print(num_list)
            with open("zadacha_42.txt", "a") as test_obj1:
                test_obj1.writelines(num_list)
        elif num_list[0] == "Two":
            num_list[0] = "Два-"
            print(num_list)
            with open("zadacha_42.txt", "a") as test_obj1:
                test_obj1.writelines(num_list)
        elif num_list[0] == "Three":
            num_list[0] = "Три-"
            print(num_list)
            with open("zadacha_42.txt", "a") as test_obj1:
                test_obj1.writelines(num_list)
        else:
            num_list[0] = "Четыре-"
            print(num_list)
            with open("zadacha_42.txt", "a") as test_obj1:
                test_obj1.writelines(num_list)



