class Matrix:
    def __init__(self, matrix):
        self.matrix = matrix

    def __str__(self):
        for row in self.matrix:
            for x in row:
                print("{:4d}".format(x), end="")
            print()

    def __add__(self, other):
        result = []
        for i in range(len(self.matrix)):
            for j in range(len(self.matrix[i])):
                print("{:4d}".format(self.matrix[i][j] + other.matrix[i][j]), end="")
            print()
        return result


matrix_1 = Matrix([[0, 1], [1, 2], [2, 3]])
matrix_2 = Matrix([[1, 1], [2, 2], [3, 3]])
print("Сумма матриц")
matrix_1 + matrix_2
print("Матрица 1")
matrix_1.__str__()
print("Матрица 2")
matrix_2.__str__()
