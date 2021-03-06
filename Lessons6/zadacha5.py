#Реализовать класс Stationery (канцелярская принадлежность). Определить в нем атрибут
# title (название) и метод draw (отрисовка). Метод выводит сообщение “Запуск отрисовки.”
# Создать три дочерних класса Pen (ручка), Pencil (карандаш), Handle (маркер).
# В каждом из классов реализовать переопределение метода draw. Для каждого из классов методы
# должен выводить уникальное сообщение. Создать экземпляры классов и проверить, что выведет
# описанный метод для каждого экземпляра.
class Stationery:
    def __init__(self, title):
        self.title = title
    def draw (self):
        print("Я рисую")

class Pen (Stationery):
    def draw (self):
        print(f"Я рисую {self.title}")

class Pencil (Stationery):
    def draw (self):
        print(f"Я рисую {self.title}")

class Handle (Stationery):
    def draw (self):
        print(f"Я рисую {self.title}")

pen1 = Pen("ручкой")
pen1.draw()
c = "*" * 40
print(f"{c}")
pen2 = Pencil("карандашом")
pen2.draw()
print(f"{c}")
pen3 = Handle("маркером")
pen3.draw()
print(f"{c}")