with open("задание_6.txt", "r+", encoding="utf-8") as file_6:
    classes = {}
    list = []
    a = file_6.readlines()
    for line in a: # создаю массив списков с предметами
        a = []
        for el in line.split():
            if ":" in el:
                a.append(el.rstrip(":"))
            if "(л)" in el:
                a.append(int(el.rstrip("(л)")))
            if "(лаб)" in el:
                a.append(int(el.rstrip("(лаб)")))
            if "(пр)" in el:
                a.append(int(el.rstrip("(пр)")))
        list.append(a)

    for i in list: # создаю словарь на основе списка
        classes[i[0]] = sum(i[1:])


print(classes)