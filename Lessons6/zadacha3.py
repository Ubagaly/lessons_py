#Реализовать базовый класс Worker (работник), в котором определить атрибуты: name, surname,
# position (должность), income (доход). Последний атрибут должен быть защищенным и ссылаться
# на словарь, содержащий элементы: оклад и премия, например, {"wage": wage, "bonus": bonus}.
# Создать класс Position (должность) на базе класса Worker. В классе Position реализовать методы
# получения полного имени сотрудника (get_full_name) и дохода с учетом премии (get_total_income).
# Проверить работу примера на реальных данных (создать экземпляры класса Position, передать данные,
# проверить значения атрибутов, вызвать методы экземпляров).
class Worker:

    def __init__(self, name, surname, position, wage, bonus):
        self.name = name.capitalize()
        self.surname = surname.capitalize()
        self.position = position
        self._income = {"wage": wage, "bonus": bonus}


class Position (Worker):

    def get_full_name(self):
        fio_info = [self.name, self.surname]
        fio_dict = {self.position: fio_info}
        fulls_name = fio_dict[self.position]
        full_name = f"{fulls_name[0]} {fulls_name[1]}"
        print(full_name)

    def get_total_income(self):
        totals_income = self._income["wage"] + self._income["bonus"]
        income_dict = {self.position: totals_income}
        total_income = income_dict[self.position]
        total_income = f"общий доход {total_income}"
        print(total_income)

person = Position("иванов", "иван", "директор", 100000, 50000)
person.get_full_name()
person.get_total_income()
c = "*" * 40
print(f"{c}")
person = Position("Петров", "Николай", "менеджер", 80000, 10000)
person.get_full_name()
person.get_total_income()
