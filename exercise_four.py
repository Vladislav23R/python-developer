user_number = int(input('Enter you number: '))

number = user_number
num_max = number % 10 # последняя цифра

while len(str(number)) != 1:
    number = number // 10 # отбрасываем последнюю цифру
    b = number % 10 #
    if num_max > b:
        continue
    else:
        num_max = b


print(num_max)
