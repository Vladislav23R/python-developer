class MyOwnErr(Exception):
    def __init__(self, text):
        self.text = text


a = input("Введите целое число: ")
b = input("Введите целое число: ")

try:
    # a, b = int(a), int(b)
    if int(b) == 0:
        raise MyOwnErr("делить на ноль нельзя")
    if a.isalpha():
        raise MyOwnErr("только числа")
    result = int(a) / int(b)
except MyOwnErr as err:
    print(err)
else:
    print(int(result))
