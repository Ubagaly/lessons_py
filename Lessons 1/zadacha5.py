# Решение 5 задания
revenue=float(input("Введите значение доходов предприятия:"))
cost=float(input("Введите значение расходов предприятия:"))
fin_res=revenue-cost
if fin_res > 0:
    r=fin_res/revenue
    print (f"Прибыль Вашего предприятия составила: {fin_res}. Рентабельность Вашего предприятия составила: {r}")
    employee=int(input("Введите численноть персонала Вашей организации:"))
    fin_res_employee=fin_res/employee
    print(f"Прибыль на одного сотрудника составила: {fin_res_employee}")


else:
    print(f"Ваше предприятие убыточно! Убыток составил: {fin_res}")