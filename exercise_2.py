from abc import ABC, abstractmethod

class Clothes(ABC):
    @abstractmethod
    def rate_cloth_1(self, x):
        pass


class Coat(Clothes):
    def rate_cloth_1(self, v):
        print(round((v / 6.5 + 0.5), 2))


class Costume(Clothes):
    def rate_cloth_1(self, h):
        print(round((h * 2 + 0.3), 2))



coat = Coat()
coat.rate_cloth_1(45)
costume = Costume()
costume.rate_cloth_1(180)