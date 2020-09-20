with open("file.txt", "w+", encoding="utf-8") as file:
    text = None
    while True:
        text = input("Введите данные: ")
        file.writelines(text + "\n")
        if len(text) == 0:
            break


