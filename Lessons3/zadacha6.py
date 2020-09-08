def int_func(text):
    return text.capitalize()

text = input("Введите слово:")
print(int_func(text))

pred = input("Введите предложение, разделяя слова пробелами:")
slovo=""
list_pred = pred.split(" ")
for el in list_pred:
    slovo = int_func(el) + " " + slovo
print(slovo)