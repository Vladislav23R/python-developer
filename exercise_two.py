list_elem = []
user_elem = None

while user_elem != 'Q':
    user_elem = input('Введите число, для выхода введите Q: ').upper()
    if user_elem != 'Q':
        list_elem.append(int(user_elem)) # добавляем элемент в список
    else:
        break

print(*list_elem) # Изначальный список

j = 0
last_elem = None

while j != len(list_elem):
    if len(list_elem) % 2 == 0: # проверяем чётность длинны списка
        list_elem[0+j:1+j], list_elem[1+j:2+j], = list_elem[1+j:2+j], list_elem[0+j:1+j] #меняем местами эл. списка
        j += 2 # шаг
    else:
        last_elem = list_elem[-1]
        list_elem.pop(-1) # при нечетном кол-ве эл убираем последний

if last_elem != None:
    list_elem.append(last_elem) # добавляем последний нечетный элемент

print(*list_elem) # Преобразованный список







