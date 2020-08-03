def int_func(*args):
    """ Функция пропускающая только латинские прописные буквы """
    args = input('Введите слово латинскими буквами: ')
    uni_list = [32, 44, 46, 33, 58, ]
    for el in range(97, 123, 1): # список строчных латинских букв в unicode, а также пробел, '.', ','
        uni_list.append(el)

    for el in args: # проверка вхождения введенных пользователем слов в латинский алфавит строчных букв
        if ord(el) in uni_list:
            continue
        else:
            return f'Ошибка.'
    return args.title()

print(int_func())



def int_func(text):
    text = text
    uni_list = [32, 44, 46, 33, 58, ]
    for el in range(97, 123, 1):
        uni_list.append(el)  # для проверки вхождения в латинский алфавит

    for el in text:
        if ord(el) in uni_list:
            continue
        else:
            return f'Ошибка'
    return text.title()

print(int_func(''))
