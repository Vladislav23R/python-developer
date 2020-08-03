summ_list = []
while True:
    ex = None
    list = (input('Введите несколько чисел через пробел:\nДля выхода введите Q ').upper()).split()
    for el in list:
        if el == 'Q':
            print('Сумма чисел: ', sum(summ_list))
            ex = el
            break
        else:
            try:
                el = int(el)
                summ_list.append(el)
            except ValueError:
                print('Вы ввели некорректное значение.')
                break
    if ex == 'Q':
        break
    print('Сумма чисел: ', sum(summ_list))





