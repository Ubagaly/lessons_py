 #Реализовать класс Matrix (матрица). Обеспечить перегрузку конструктора класса
 # (метод __init__()), который должен принимать данные (список списков) для формирования матрицы.
 #Подсказка: матрица — система некоторых математических величин, расположенных в виде прямоугольной схемы.
#Следующий шаг — реализовать перегрузку метода __str__() для вывода матрицы в привычном виде.
#Далее реализовать перегрузку метода __add__() для реализации операции сложения двух объектов класса
 # Matrix (двух матриц). Результатом сложения должна быть новая матрица.
#Подсказка: сложение элементов матриц выполнять поэлементно — первый элемент первой строки первой
 # матрицы складываем с первым элементом первой строки второй матрицы и т.д.

class Matrix:
    def __init__(self, matrix_str):
        self.matrix_str = matrix_str
        self.a = list

    def __str__(self):
        for line in range(len(self.matrix_str)):
            for el in range (len(self.matrix_str[line])):
                print(self.matrix_str[line][el], end=' ')
            print()
        return str()

    def __add__(self, other):
        result = []
        numbers = []
        for line in range(len(self.matrix_str)):
            for el in range(len(self.matrix_str[0])):
                summer = self.matrix_str[line][el] + other.matrix_str[line][el]
                numbers.append(summer)
                if len(numbers) == len(self.matrix_str):
                    result.append(numbers)
                    numbers = []

        return Matrix(result)



m1 = Matrix([[3, 5, 6], [1, 8, 10], [11, 4, 2]])
m2 = Matrix([[1, 2, 3], [4, 7, 6], [2, 3, 9]])
print(m1)
print(m2)
print(m1 + m2)