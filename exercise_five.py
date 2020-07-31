rating = [7, 5, 3, 3, 2]
user_app = None

while user_app != 'Q':
    user_app = input('Введите элемент рейтинга.\nДля завершения введите Q: ').upper()
    if user_app != 'Q':
        rating.append(float(user_app))
        for i in range(len(rating)): # кол-во кругой для сравнения
            for el in range(len(rating) - i - 1): # кол-во проверок
                if rating[el] < rating[el + 1]: # сравниваем эл-ты списка
                    rating[el], rating[el + 1] = rating[el + 1], rating[el] # меняем местами элементы

print(*rating)





# while user_app != 'Q':
#     user_app = input('Введите элемент рейтинга.\nДля завершения введите Q: ').upper()
#     if user_app != 'Q':
#         if int(user_app) > max(rating):
#             rating.insert(0, float(user_app))
#         elif int(user_app) < min(rating):
#             rating.append(float(user_app))
#         else:
#             a = rating.count(int(user_app))
#             b = rating.index(int(user_app))
#             rating.insert(b + a, float(user_app))



# print(*rating)

# while user_app != 'Q':
#     user_app = input('Введите элемент рейтинга, для завершения введите Q: ').upper()
#     if user_app != 'Q':
#         print(int(user_app) in rating)
#         rating.append(int(user_app)) if min(rating) > int(user_app) else rating.insert(0, int(user_app)) if max(rating) < int(user_app) else 0
#
#         print(*rating)

# while user_app != 'Q':
#     user_app = input('Введите элемент рейтинга, для завершения введите Q: ').upper()
#     if user_app != 'Q':
#         rating.append(int(user_app))
#         i = 0
#         while i != len(rating):
#             min = 0
#             if rating[i] <= min:
#                 min = rating[i]
#                 rating.append(min)
#                 i += 1
#             else:
#                 rating.insert(0, rating[i])
#                 i += 1

# print(rating)
