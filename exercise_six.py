a = float(input('Enter the result in kilometers for the first day: '))
b = float(input('How many kilometers do you want to run: '))

day = 1

while a <= b:
    a = a + (a * 0.1)
    day += 1
    print(f'{day}-й день спортсмен пробежал {round(a, 2)} км')

print(f'На {day}-й день спортсмен достиг результата - не менее {b} км')

