class Data:
    def __init__(self, data):
        self.data = data

    @classmethod
    def integer(cls, data):
        try:
            result = [int(i) for i in data.split("-")]
            return result
        except (ValueError, TypeError, UnboundLocalError):
            print("Дата должна быть числами")


    @staticmethod
    def validation(data):
        try:
            data = data.split("-")
            if 1 <= int(data[0]) <= 31 and 1 <= int(data[1]) <= 12 and 0 <= int(data[2]) <= 2020:
                return f"Дата: {data[0]}-{data[1]}-{data[2]}"
        except (ValueError, TypeError):
            return f"Несуществующая дата."



obj = Data(input("Введите дату в формате дд-мм-гггг: "))
# print(obj.data)
# print(obj.integer(obj.data))
print(Data.validation(obj.data))