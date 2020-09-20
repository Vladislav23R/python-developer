with open("task5.txt", "w+", encoding="utf-8") as file5:
    try:
        content = input("введите числа через пробел: ")
        file5.write(content)
        file5.seek(0)
        read = file5.read()
        print(read)
        summ = 0
        for i in read.split():
            summ += int(i)
        print(summ)
    except ValueError:
        print("Only numeric")
