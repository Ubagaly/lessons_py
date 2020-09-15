import re
with open("zadacha_6.txt", "r") as test_obj:
    for line in test_obj:
        slov_list = line.split(":")
        slov_list[-1] = slov_list[-1].strip()
        for el in slov_list[1]:
            el

        re.findall
        #slov_dict = dict(slov_list)
        print(slov_list)
