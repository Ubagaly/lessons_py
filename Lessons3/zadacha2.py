def person (name, surname, data, city, my_mail, tel_number):
    return name.capitalize() + " " + surname.capitalize() + " " + data + "г.р. г. " + city.capitalize() + " " + my_mail + " " + tel_number

a = input("Введите имя:")
b = input("Введите фамилию:")
c = input("Введите год рождения:")
d = input("Введите город рождения:")
e = input("Введите e-mail:")
f = input("Введите телефонный номер:")
print(person(name=a, surname=b, data=c, city=d, my_mail=e, tel_number=f))
