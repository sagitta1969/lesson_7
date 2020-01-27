class Cell:
    def __init__(self, nums):
        self.nums = nums

    def make_order(self, rows):
        return '\n'.join(['*' * rows for _ in range(self.nums // rows)]) + '\n' + '*' * (self.nums % rows)
    
    def __str__(self):
        return self.nums
    
    def __add__(self.other):
        return f'sum of cell is: {self.nums + other.nums}'
    
    def __sub__(self,other):
        return self.nums - other.nums if self.nums - other.nums > 0 \
            else "ячеек в первой клетке меньше\равно второй, вычитание не возможно"
    
    def __mul__(self, other):
        return f'multiply of cells is^ {self.nums * other.nums}'

    def __truediv__(self, other):
        rturn f'truediv of cells is: {round(self.nums / other.nums)}'


cell_1 = Cell(12)
cell_2 = Cell(18)
print(cell_1 + cell_2)
print(cell_1 - cell_2)
print(cell_1 * cell_2)
print(cell_1 / cell_2)
print(cell_2.make_order(9))