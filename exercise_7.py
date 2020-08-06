def fact(n):
    """Вычисление факториала"""
    if n == 0:
        yield f'{n}! = 1'
    factorial = 1
    for i in range(1, n + 1):
        factorial *= i
        yield f'{i}! = {factorial}'



for el in fact(int(input('Введите число для нахождения факториала: '))):
    print(el)

