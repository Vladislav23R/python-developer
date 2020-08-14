class Road:
    # lenght - длинна асфальта
    # wight - ширина асфальта
    # weight_1_kv_m - количество кг асфальта на 1 кв м
    # blade_thickness - толщина покрытия
    
    def __init__(self, lenght, wight, weight_1_kv_m, blade_thickness):
        self._lenght = lenght
        self._wight = wight
        self._weight_1_kv_m = weight_1_kv_m
        self._blade_thickness = blade_thickness

    def mass(self):
        mas = (self._lenght * self._wight * self._weight_1_kv_m * self._blade_thickness)/1000
        return f"Масса асфальта длиной {self._lenght}м, шириной {self._wight}м, " \
               f"массой покрытия одного кв метра {self._weight_1_kv_m}кг " \
               f"и толщиной покрытия {self._blade_thickness}см = {mas} тонн"

try:
    road = Road(float(input("Введите длинну асфальта: ")), float(input("Введите ширину асфальта: ")),
                float(input("Введите количество кг асфальта на 1 кв.м: ")),
                float(input("Введите толщину полотна в см: ")))
    print(road.mass())
except ValueError:
    print('Введите число!')