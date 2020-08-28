# Решение 3 задания
a=int(input("Задайте любое число :"))
c=int(input("Задайте max колличество n :"))
n=0
sum=0
st=1
while st <= c:
    n=int(f"{n}{a}")
    sum=sum+n
    st=st+1
else:
    print(f"Сумма равна: {sum}")