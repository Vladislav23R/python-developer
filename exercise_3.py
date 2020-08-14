class Worker:
    def __init__(self, name, surname, position, _income):
        self.name = name
        self.surname = surname
        self.position = position
        self._income = _income

class Position(Worker):
    def get_full_name(self):
        return f"Имя: {self.name}\nФамилия:{self.surname}"

    def get_total_income(self):
        sum = self._income["wage"] + self._income["bonus"]
        return f"Доход сотрудника = {sum}"

try:
    user_1 = Position(input("Введите имя: "), input("Введите фамилию: "), input("Введите должность: "),
                      _income={"wage": float(input("Введите оклад: ")), "bonus": float(input("Введите премию: "))})
    print(user_1.get_full_name())
    print(user_1.get_total_income())
except ValueError:
    print("Ошибка")





