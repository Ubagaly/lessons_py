import json
prib_dict = {}
sum_prib = 0
num = 0

fin_result = 0

with open("zadacha_7.txt", "r") as test_obj:
    for line in test_obj:
        slov_list = line.split(" ")
        slov_list[-1] = slov_list[-1].strip()
        fin_result = int(slov_list[2]) - int(slov_list[3])
        if fin_result >= 0:
            prib_dict.update({slov_list[0]:fin_result})
            num = num + 1
            sum_prib = (sum_prib + fin_result)/num

        else:prib_dict.update({slov_list[0]:fin_result})
    sr_dict = {"Средняя прибыль": sum_prib}
    fin_list = [prib_dict, sr_dict]
    print(fin_list)

with open("zadacha_7.json", "w") as write_f:
    json.dump(fin_list, write_f)

