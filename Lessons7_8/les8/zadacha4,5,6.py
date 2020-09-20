#Начните работу над проектом «Склад оргтехники». Создайте класс, описывающий склад.
# А также класс «Оргтехника», который будет базовым для классов-наследников.
# Эти классы — конкретные типы оргтехники (принтер, сканер, ксерокс). В базовом классе определить
# параметры, общие для приведенных типов. В классах-наследниках реализовать параметры, уникальные
# для каждого типа оргтехники.
#5. Продолжить работу над первым заданием. Разработать методы, отвечающие за приём оргтехники на склад и передачу в
# определенное подразделение компании. Для хранения данных о наименовании и количестве единиц оргтехники,
# а также других данных, можно использовать любую подходящую структуру, например словарь.
#6. Продолжить работу над вторым заданием. Реализуйте механизм валидации вводимых пользователем данных. Например,
# для указания количества принтеров, отправленных на склад, нельзя использовать строковый тип данных.

from abc import abstractmethod, ABC

class VolumeError(Exception):
    def __init__(self, txt):
        self.txt = txt

class MinError(Exception):
    def __init__(self, txt):
        self.txt = txt

class Sklad(ABC):

    @abstractmethod
    def ostatok(self):
        pass

    @abstractmethod
    def volume(self):
        pass

    @abstractmethod
    def volume_sum(self):
        pass


class Orgtexnika(Sklad):
    volume_max = 1000
    volume_nast = 0
    volume_pr = 0

    def __init__(self, num, a, b, c):
        try:
            self.a = int(a)
            self.b = int(b)
            self.c = int(c)
            self.num = int(num)
        except ValueError:
            print("Вы ввели не целые числа, задайте параметры заново")
        except NameError:
            print("Вы ввели не целые числа, задайте параметры заново")


    def volume(self):
        volume_pr = self.num * self.a * self.b * self.c
        return volume_pr

    def volume_sum (self):
        self.volume_nast = self.volume_nast + self.volume()
        return self.volume_nast

    def ostatok(self, param):
        try:
            self.param = int(param)
            if self.param >= 0:
                self.num += self.param
                if self.volume_sum() > self.volume_max:
                    raise VolumeError("Склад переполнен всё не поместится")
                else:
                    return self.num
            else:
                self.num -= abs(self.param)
                if self.num < 0:
                    raise MinError("Техники нет на складе")
                else:
                    return self.num
        except VolumeError as err:
            print(err)
        except MinError as err:
            print(err)



class Printer(Orgtexnika):
    def volume_sums(self):
        return f"Объем занятой площади составляет {super().volume_sum()}"

    def ostatoks(self, param):
         return f"Остаток принтеров на складе составляет {super().ostatok(param)}"

class Skaner(Orgtexnika):
    def volume_sums(self):
        return f"Объем занятой площади составляет {super().volume_sum()}"

    def ostatoks(self, param):
         return f"Остаток сканеров на складе составляет {super().ostatok(param)}"

class Kseroks(Orgtexnika):
    def volume_sums(self):
        return f"Объем занятой площади составляет {super().volume_sum()}"

    def ostatoks(self, param):
         return f"Остаток ксероксов на складе составляет {super().ostatok(param)}"

# num - заданный остаток товара на складе
# a,b,c - параметры длина, ширина, высота для определения занимаемого объема единицы оргтехники
#param - если приняли на склад то число положительное, отдали со склада число отрицательное
p = Printer(3, 3, 3, 5)
s = Skaner(1, 5, 1, 6)
k = Kseroks(2, 3, 1, 5)
print (p.volume_sums())
print (p.ostatoks(4))
print (s.volume_sums())
print (s.ostatoks(4))
print (k.volume_sums())
print (k.ostatoks(4))

