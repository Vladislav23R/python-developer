class ComplexNum:
    def __init__(self, param):
        self.param = param

    def __str__(self):
        return f"{self.param}"

    def __add__(self, other):
        return ComplexNum(self.param + other.param)


    def __mul__(self, other):
        return ComplexNum(self.param * other.param)


num_1 = ComplexNum(2 + 1j)
num_2 = ComplexNum(3 + 5j)
num_3 = ComplexNum(3 + 1j)
num_4 = ComplexNum(2 - 3j)
print(num_1 + num_2)
print(num_3 * num_4)
