class Stationery:
    def __init__(self, title):
        self.title = title

    def draw(self):
        return f"Запуск отрисовки."


class Pen(Stationery):
    def draw(self):
        return f"Начинаем рисовать ручкой."


class Pencil(Stationery):
    def draw(self):
        return f"В ход идет карандаш."


class Handle(Stationery):
    def draw(self):
        return f"Воспользуемся маркером."


s = Stationery('go')
print(s.draw())
pen = Pen("ручка")
print(pen.draw())
pencil = Pencil("карандаш")
print(pencil.draw())
handle = Handle("маркер")
print(handle.draw())
