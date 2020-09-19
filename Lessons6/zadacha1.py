#Создать класс TrafficLight (светофор) и определить у него один атрибут color (цвет) и метод
# running (запуск). Атрибут реализовать как приватный. В рамках метода реализовать переключение
# светофора в режимы: красный, желтый, зеленый. Продолжительность первого состояния (красный)
# составляет 7 секунд, второго (желтый) — 2 секунды, третьего (зеленый) — на ваше усмотрение.
# Переключение между режимами должно осуществляться только в указанном порядке (красный, желтый, зеленый).
# Проверить работу примера, создав экземпляр и вызвав описанный метод.
import time

class TrafficLight:
    def __init__(self, color):
        self.__color = color

    def running(self):
        print(f"Горит {self.__color} свет")


color_red = TrafficLight(color="красный")
color_yellow = TrafficLight(color="желтый")
color_green = TrafficLight(color="зелёный")

#вариант 1
color_red.running()
time.sleep(7)
color_yellow.running()
time.sleep(2)
color_green.running()
time.sleep(5)

#вариант 2 
stop = 7 + time.time()
while time.time() <= stop:
    color_red.running()
stop = 2 + time.time()
while time.time() <= stop:
    color_yellow.running()
stop = 5 + time.time()
while time.time() <= stop:
    color_green.running()

