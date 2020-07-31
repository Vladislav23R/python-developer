user_str = (input("Введите несколько слов через пробел: ")).split()
for index, value in enumerate(user_str):
    index += 1 # корректная нумерация
    value = value[:10] # ограничиваем кол-во символов
    print(index, value)



