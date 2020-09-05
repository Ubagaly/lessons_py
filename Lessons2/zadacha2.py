#Решение к задачи 2:
pred = input("Заполите список, перечисляя элементы списка через запятую : ")
list_pred = pred.split(",")
print(list_pred)
num = 0
for el in range(int(len(list_pred)/2)):
    list_pred[num],list_pred[num+1]=list_pred[num+1],list_pred[num]
    num = num + 2

print(list_pred)

