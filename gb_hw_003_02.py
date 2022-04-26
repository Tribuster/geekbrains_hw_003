#    2. Выполнить функцию, которая принимает несколько параметров, описывающих данные пользователя:
#   имя, фамилия, год рождения, город проживания, email, телефон.
#   Функция должна принимать параметры как именованные аргументы.
#   Осуществить вывод данных о пользователе одной строкой.

def user_data (name_user, lastname_user, year_of_birth, city_user, email_user, number_of_phone):
    print(f'Имя: {name_user} Фамилия: {lastname_user} Год рождения: {year_of_birth} год '
            f'Город проживания: {city_user} e-mail: {email_user} Номер телефона: {number_of_phone}')


user_data(name_user = input('Введите ваше имя: '),
          lastname_user = input('Введите вашу фамилию: '),
          year_of_birth = input('Введите год вашего рождения: '),
          city_user = input('Введите наименование города, в котором вы проживаете: '),
          email_user = input('Введите ваш e-mail: '),
          number_of_phone = input('Введите номер вашего телефона: '))