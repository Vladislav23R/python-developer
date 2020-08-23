class Exception(Exception):
    def __init__(self, text):
        self.text = text


list = []
user_input = None
while user_input != "STOP":
    try:
        user_input = input("Введите значение:\nДля завершения введите STOP: ").upper()
        if user_input == "STOP":
            break
        if user_input.isalpha():
            raise Exception("в список пойдут только числа!")
        list.append(int(user_input))
    except Exception as err:
        print(err)

print(list)
