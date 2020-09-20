# вариант 1

# with open("задание_4.txt", "r+", encoding="utf-8") as file:
#     dict = {"One": "Один - 1", "Two": "Два - 2", "Three": "Три - 3", "Four": "Четыре - 4"}
#     list = []
#     for line in file:
#         for i in line.split(" "):
#             for key in dict.keys():
#                 if i == key:
#                     list.append(dict[key])
#     print(list)
#     with open("задание_4_1.txt", "w+", encoding="utf-8") as new_file:
#         for i in list:
#             print(i, file=new_file)



 # вариант 2
with open("задание_4.txt", "r+", encoding="utf-8") as file:
    dict = {"One": "Один", "Two": "Два", "Three": "Три", "Four": "Четыре"}
    with open("задание_4_2.txt", "w+", encoding="utf-8") as new_file_1:
        for line in file:
            for i in line.split(" "):
                if i in dict.keys():
                    new_file_1.write(dict[i] + " ")
                elif i == "-":
                    new_file_1.write(i + " ")
                else:
                    new_file_1.write(i)







