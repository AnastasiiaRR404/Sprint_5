from random import randint

def new_email():
    login = 'palagina' + str(randint(100, 999)) + '@ya.ru'
    return login