# number_1 = [el for el in range(20, 241, 20)] # кратное 20
# number_2 = [el for el in range(20, 241, 21)] # кратное 21
number = [el for el in range(20, 241) if el % 20 == 0 or el % 21 == 0] # кратное 20 и 21
# print(number_1)
# print(number_2)
print(number)