from itertools import count, cycle

print('Задание 1.\n')
my_list = []
a = int(input('Введите на каком числе закончить: '))
for i in count(int(input('Введите с какого числа начать: '))):
    if i > a:
        break
    print(i)
    my_list.append(i)


print('-' * 33, "\nЗадание 2.\n")


m = 0
for i in cycle(my_list):
    if m > 10:
        break
    print(i)
    m += 1

