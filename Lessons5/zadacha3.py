with open("zadacha_3.txt", "r") as test_obj:
    sum_str = 0
    sr_zar = 0
    num = 0
    for line in test_obj:
        sum_list = line.split(",")
        sum_str = sum_str + int(sum_list[1])
        num = num + 1
        if int(sum_list[1]) >= 20000:
            print(sum_list[0])
        
    sr_zar = sum_str/num
    print(f"Средняя зар. плата состовила: {sr_zar}")
