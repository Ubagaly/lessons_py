with open("zadacha_2.txt", "r") as test_obj:
    sum_str = 0
    for line in test_obj:
        sum_str = sum_str + 1
        sum_list = line.split(" ")
        sum_sl = len(sum_list)
        print(line)
        print(f"В {sum_str} строке {sum_sl} слов(а)")