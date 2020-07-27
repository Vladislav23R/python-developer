time_user = int(input('Enter time in seconds:  '))


# 1 min = 60 sec
# 1 hour = 60 min
# 1 hour = 3600 sec
h = time_user // 3600
m = (time_user - h * 3600) // 60
s = (time_user - h * 3600) - (m * 60)


print(f'{h}:{m}:{s}')
print('{:02d}:{:02d}:{:02d}'.format(h, m, s))