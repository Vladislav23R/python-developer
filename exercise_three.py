list = [
    ['зима', 1, 2, 12],
    ['весна', 3, 4, 5],
    ['лето', 6, 7, 8],
    ['осень', 9, 10, 11]
]

user_month = int(input('Введите номер месяца от 1 до 12: '))
while True:
    if 1 <= user_month <= 12:
        break
    else:
        print("Не корректное значение, введите цело число от 1 до 12")
        user_month = int(input('Введите номер месяца от 1 до 12: '))
        continue

i = 0
while True:
    if user_month in list[0 + i]:
        print('Время года:', list[0 + i][0])
        break
    else:
        i += 1


dict = {
    'зима': [1, 2, 12],
    'весна': [3, 4, 5],
    'лето': [6, 7, 8],
    'осень': [9, 10, 11]
}

for key, value in dict.items():
    if user_month in value[::]:
        print('Время года:', key[::])
