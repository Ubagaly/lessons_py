# Решение 4 задания
a=int(input("Введите любое целое число:"))
b=0
max=0

while a>10:
    b=a%10
    a = a // 10
    if b>max:
        max=b

else:
    if a>max:
        max=a
    print(f"Максимальное число: {max}")