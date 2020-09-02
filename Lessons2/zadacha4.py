#Решение к задачи 4:
# 1 вариант
pred = input("Введите любое предложение, разделяя слова пробелами: ")
list_pred = pred.split()
for ind, el in enumerate(list_pred):
    ind = ind + 1
    print(ind, el[:10])

# 2 вариант (сделала сначала его, потом в методичке нашла как можно проще сделать...)
#pred=input("Введите любое предложение, разделяя слова пробелами: ")
#list_pred = pred.split()
#list_size = len(list_pred)
#num = 1
#q = 0
#for el in list_pred:
    #slovo = list_pred[q]
    #print(f"{num}.{slovo[:10]}")
    #if num < list_size:
        #num = num + 1
        #q = q + 1


