#К 7 УРОКУ!!!
# Реализовать программу работы с органическими клетками. Необходимо создать класс Клетка.
# В его конструкторе инициализировать параметр, соответствующий количеству клеток (целое число).
# В классе должны быть реализованы методы перегрузки арифметических операторов: сложение (__add__()),
# вычитание (__sub__()), умножение (__mul__()), деление (__truediv__()).Данные методы должны
# применяться только к клеткам и выполнять увеличение, уменьшение, умножение и обычное
# (не целочисленное) деление клеток, соответственно. В методе деления должно осуществляться округление
# значения до целого числа.
class Kletka:
    def __init__(self, param):
        self.param = param

    def __add__(self, other):
        return self.param + other.param

    def __mul__(self, other):
        return self.param * other.param

    def __truediv__(self, other):
        return self.param / other.param

    def __sub__(self, other):
        raz = self.param - other.param
        if raz > 0:
            return raz
        else:print("Задайте другие значения количества клеток")

    def make_order(self, row):
        kolichestvo = "/n".join(["*" * row for _ in range(self.param//row)])
        os = self.param % row
        ostatok = "*" * os
        return f"{kolichestvo}/n{ostatok}"



k1 = Kletka(35)
k2 = Kletka(3)
print(k1 * k2)
print(k1-k2)
print(k1.make_order(8))
