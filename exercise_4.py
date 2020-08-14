from random import randint, choice

class Car:
    def __init__(self, speed, color, name, is_police=bool):
        self.speed = speed
        self.color = color
        self.name = name
        self.is_police = is_police

    def go(self):
        print(f"Машина: {self.name}\nЦвет: {self.color}")
        print("Поехали!")

    def stop(self):
        print("Стоп машина!")
        print("-" * 30)

    def turn(self, direction=None):
        direction  = ["Прямо", "Назад", "Направо", "Налево"]
        print(f"Направление = {choice(direction)}")


    def show_speed(self):
        self.speed = randint(1, self.speed)
        print(f"Ваша скорость = {self.speed}")


class TownCar(Car):
    def show_speed(self):
        self.speed = randint(1, self.speed)
        if self.speed > 60:
            print("Вы превысили скорость!\nОграничение 60 км/ч")
        return f"Ваша скорость = {self.speed}"


class SportCar(Car):
    pass

class WorkCar(Car):
    def show_speed(self):
        self.speed = randint(1, self.speed)
        if self.speed > 40:
            print("Вы превысили скорость!\nОграничение 60 км/ч")
        return f"Ваша скорость = {self.speed}"
#
class PoliceCar(Car):
    pass



town_c = TownCar(80, "black", "Ford", False)
town_c.go()
print(town_c.show_speed())
town_c.turn()
town_c.stop()


sport_c = SportCar(600, "red", "Ferrari", False)
sport_c.go()
sport_c.show_speed()
sport_c.turn()
sport_c.stop()


work_c = WorkCar(70, "yellow", "CAT", False)
work_c.go()
print(work_c.show_speed())
work_c.turn()
work_c.stop()

police_c = PoliceCar(400, "white blue", "Doodge", True)
police_c.go()
police_c.show_speed()
police_c.turn()
police_c.stop()


