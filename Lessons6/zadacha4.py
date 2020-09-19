#Реализуйте базовый класс Car. У данного класса должны быть следующие атрибуты: speed,
# color, name, is_police (булево).
# А также методы: go, stop, turn(direction), которые должны сообщать, что машина поехала,
# остановилась, повернула (куда). Опишите несколько дочерних классов: TownCar, SportCar, WorkCar,
# PoliceCar. Добавьте в базовый класс метод show_speed, который должен показывать текущую скорость
# автомобиля. Для классов TownCar и WorkCar переопределите метод show_speed. При значении скорости
# свыше 60 (TownCar) и 40 (WorkCar) должно выводиться сообщение о превышении скорости.
#Создайте экземпляры классов, передайте значения атрибутов. Выполните доступ к атрибутам, выведите
#результат. Выполните вызов методов и также покажите результат.
try:
    class Car:
        speed = int(input("С какой скоростью движется автомобиль?"))
        color = input("Какого цвета машина?")
        name = input("Автомобиль какой марки?")
        is_police = input("Это полиция?(Да/Нет)")
        if is_police == "Да":
            is_police = True
        else: is_police = False

        def go(self):
            print("Машина поехала")

        def stop(self):
            print("Машина остановилась")

        def turn(self):
            print("Машина повернула")

        def show_speed(self):
            print(f"Атомобиль {self.name} {self.color} eдет со скоростью {self.speed} км.ч.")


    class WorkCar(Car):
        def individ(self):
            print("Это рабочая машина")

        def show_speed(self):
            if self.speed > 40:
                print(f"Вы превысили скорость! Ваш автомобиль едет {self.speed}")
            else:
                print(f"Атомобиль {self.name} {self.color} eдет со скоростью {self.speed} км.ч.")


    class TownCar(Car):
        def individ(self):
            print("Это городской автомобиль")

        def show_speed(self):
            if self.speed > 60:
                print(f"Вы превысили скорость! Ваш автомобиль едет {self.speed}")
            else:
                print(f"Атомобиль {self.name} {self.color} eдет со скоростью {self.speed} км.ч.")


    class SportCar(Car):
        def individ(self):
            print("Это спорт кар! Он мчится очень быстро")


    class PoliceCar(Car):
        def individ(self):
            print("Это Полиция! Остановитесь!")


    c = "*" * 40
    print(f"{c}")
    avto = Car()
    avto.is_police = str(avto.is_police)
    print(avto.is_police)
    if avto.is_police == "True":
        avto4 = PoliceCar()
        print(f"{avto4.name} {avto4.color}")
        avto4.individ()
        avto4.go()
        avto4.show_speed()
        avto4.stop()
        print(f"{c}")

    else:
        avto1 = SportCar()
        print(f"{avto1.name} {avto1.color}")
        avto1.individ()
        avto1.go()
        avto1.show_speed()
        avto1.stop()
        print(f"{c}")
        avto2 = TownCar()
        print(f"{avto2.name} {avto2.color}")
        avto2.turn()
        avto2.show_speed()
        avto2.stop()
        print(f"{c}")
        avto3 = WorkCar()
        print(f"{avto3.name} {avto3.color}")
        avto3.individ()
        avto3.go()
        avto3.show_speed()
        avto3.turn()
        print(f"{c}")

except ValueError as error:
    print("Ошибка: Не верно введено значение.Введите число")