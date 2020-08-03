# 1 вариант
def div(a = int(input('Enret number: ')), b = int(input('Enret number: '))):
    if a == 0 or b == 0:
        return f'Делить на ноль нельзя!'
    else:
        result = a / b
        return result

print(div())



# 2 вариант
def div():
    """ Деление двух чисел """
    a = input('Enret number: ')
    b = input('Enret number: ')
    try:
        result = int(a) / int(b)
        return result
    except ZeroDivisionError:
        return f"На ноль делить нельзя!"
    except ValueError:
        return f'Только числа.'

print(div())



