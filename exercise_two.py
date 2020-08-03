def user_info(first_name, surname, date_of_birth, town, email, telephone):
    """ Информация о пользователе """
    print(f'{first_name} {surname}, {date_of_birth} г.р., {town}, Email: {email}, Номер телефона: {telephone}')

user_info(first_name=input('Введите имя: '), surname=input('Введите фамилию: '),
          date_of_birth=input('Введите дату рождения: '), telephone=input('Введите номер телефона: '),
          town=input('Введите название города: '), email=input('Введите email: '))
