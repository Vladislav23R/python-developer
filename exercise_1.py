from sys import argv

def wages(argv):
    return float(rub_hour) * float(hour) + float(bonus)

name, rub_hour, hour, bonus = argv


print(f'Отработано часов: {rub_hour}')
print(f'Ставка: {hour}')
print(f'Премия: {bonus}')
print(f'Заработная плата составила: {wages(argv)}')