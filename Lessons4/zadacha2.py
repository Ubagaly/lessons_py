my_list = [300, 2, 12, 40, 1, 1, 4, 10, 7, 1, 78, 120, 55]
# 1 вариант
num = 0
news_list=[]
for el in range(int(len(my_list)-1)):
    if my_list[num] < my_list[num+1]:
        news_list.append(my_list[num+1])
        num = num+1
    else:num = num+1
# 2 вариант
new_list = [my_list[el+1] for el in range(int(len(my_list)-1)) if my_list[el] < my_list[el+1]]

print(news_list)
print(new_list)