# 1 вариант
def my_func(a, b, c):
    """ Сумма наибольших двух элементов"""
    list = []
    list.append(a)
    list.append(b)
    list.append(c)
    min(list)
    list.remove(min(list))
    print(sum(list))

my_func(10, 50, 2)
my_func(1, 50, 2)
my_func(25, 1, 2)


# 2 вариант
def my_func1(a, b, c):
    """ Сумма наибольших двух элементов"""
    list = []
    list.append(a + b)
    list.append(b + c)
    list.append(c + a)
    print(max(list))

my_func1(10, 6, 5)
my_func1(10, 12, 15)
my_func1(10, 2, 5)


# 3 вариант
def my_func2(a, b, c):
    """ Сумма наибольших двух элементов"""
    if a > c and b > c:
        result = a + b
        return f'{result}'
    elif b > a and c > a:
        result = b + c
        return f'{result}'
    else:
        result = a + c
        return f'{result}'

print(my_func2(2, 10, 1))
print(my_func2(2, 10, 5))
print(my_func2(12, 10, 12))