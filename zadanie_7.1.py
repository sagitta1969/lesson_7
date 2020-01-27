class Matrix:
    def __init__(self, args):
        self.args = args

    def __str__(self):
        return str('\n' .join(['\t' .join([str(j) for j in i]) for i in self.args]))

    def __add__(self, other):
        result = []
        num = []
        if len(self.args) == len(other.args): #проверка длинн матриц
            for i in range(len(self.args)): # перебирает елементы списка
                for j in range(len(self.args[i])): # перебирает элементы вложенных списков
                    num.append(self.args[i][j] + other.args[i][j]) # формирует список num
                    if len(num) == len (self.args[i]):
                        result.append(num)
                        num = []
        else:
            print("матрицы должны быть одинакового размера")
        return result


my_matrix1 = Matrix([[1, 2], 
                     [3, 4], 
                     [5, 6]])

my_matrix2 = Matrix([[9, 8],
                     [7, 6],
                     [5, 4]])
print(my_matrix1)
print(my_matrix2)
print(my_matrix1 + my_matrix2)