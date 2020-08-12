# 4 урок - задание №2 и №4.

# Задание № 2
list = [300, 2, 12, 44, 1, 1, 4, 10, 7, 1, 78, 123, 55]
a = [list[i] for i in range(1, len(list)) if list[i] > list[i - 1]]
print(a)

# Задание № 4
list_1 = [2, 2, 2, 7, 23, 1, 44, 44, 3, 2, 10, 7, 4, 11]
b = [num for num in list_1 if list_1.count(num) == 1]
print(b)

