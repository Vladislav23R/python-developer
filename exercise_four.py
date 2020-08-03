def my_pow_func(x=None, y=None):
    """ Возведение в отрицательную степень """
    try:
        x = int(input('Введите положительное число: '))
        y = int(input("Введите отрицательное целое число: "))
    except ValueError:
        return f"Введите числа."

    c = x
    i = 1
    while i != abs(y):
        c = c * x
        i += 1
    result = 1 / c
    return f"{result}"

print(my_pow_func())

