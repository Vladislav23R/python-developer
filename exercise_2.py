first_list = [300, 2, 12, 44, 1, 1, 4, 10, 7, 1, 78, 123, 55]

list_2 = []
a = [el for el in first_list]
print(a)
for i in range(1, len(a)):
    if a[i] > a[i-1]:
        list_2.append(a[i])

print(list_2)






