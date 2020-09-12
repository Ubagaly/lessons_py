my_list = [2, 2, 2, 2, 23, 1, 44, 44, 3, 2, 10, 7, 4, 11, 15, 15, 25]

#1 вариант(последовательность сохранена, повторяющиеся элементы НЕ выводятся)
newss_list = [my_list[el] for el in range(len(my_list)) if my_list.count(my_list[el]) == 1]
print(newss_list)

# 2 вариант (последовательность сохранена, повторяющиеся элементы выводятся 1 раз)
news_list = list(dict.fromkeys(my_list))
print (news_list)

#3 вариант (последовательность не сохранена, повторяющиеся элементы выводятся 1 раз)
new_list = list(set(my_list))
print (new_list)