with open("задание_3.txt", "r+", encoding="utf-8") as file:
    staf = []
    for line in file:
        if line == "\n":
            break
        if int(line.split()[1]) < 20000:
            staf.append(line.split()[0])
    print(f"Сотрудники чьи зарплаты меньше 20000 тысяч: ")
    for i in staf:
        print(i)
