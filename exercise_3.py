class Ceil:
    def __init__(self, ceil):
        self.ceil = ceil


    def __str__(self):
        return f"{self.ceil}"


    def __add__(self, other):
        return Ceil(self.ceil + other.ceil)


    def __sub__(self, other):
        if self.ceil >= other.ceil:
            return Ceil(self.ceil - other.ceil)
        else:
            if self.ceil < other.ceil:
                print(f"Из меньшего нельзя вычитать большее\nНо мы можем поменять их местами")
                return Ceil(other.ceil - self.ceil)


    def __mul__(self, other):
        return Ceil(self.ceil * other.ceil)


    def __floordiv__(self, other):
        if self.ceil > 0 and other.ceil > 0:
            return Ceil(self.ceil // other.ceil)
        else:
            return f"На 0 делить нельзя"


    def make_order(self, a):
        for i in range(1, (self.ceil + 1)):
            if i % a == 0:
                print("*" * a)
            if i == self.ceil:
                print("*" * (i % a))
                break

ceil_1 = Ceil(26)
ceil_2 = Ceil(15)
# print(ceil_1 + ceil_2)
# print(ceil_1 - ceil_2)
# print(ceil_1 * ceil_2)
# print(ceil_1 // ceil_2)
ceil_1.make_order(5)
print()
ceil_2.make_order(2)


