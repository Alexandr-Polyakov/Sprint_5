from random import randint

class Person:
    user_name = 'Александр'
    email = 'AlexandrPolyakov299@yandex.ru'
    password = 'Qwedsa213'

class RandomData:
    user_name = 'Тест'
    email = f'test{randint(0, 999)}@yandex.ru'
    password = f'{randint(0, 999)}Qwedsa'