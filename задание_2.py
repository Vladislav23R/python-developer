with open("задание_2.txt", "r+", encoding="utf-8") as file:
    strings = 0
    words = 0
    for line in file:
        strings += 1
        for word in line.split():
            words += 1

    print(f"{strings = }, {words = }")