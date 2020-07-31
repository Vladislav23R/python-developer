list = [12, 54.12, 'str', True, (12, 'Hello'), {'name': 'Lex', 'age': 25}, ['str', 12], {12, 44.23, 'set'}]

for index, value in enumerate(list):
    index += 1 # корректное отоброжение нумерации с 1, а не 0
    print(index, type(value))


