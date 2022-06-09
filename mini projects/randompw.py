import string 
import random

characters = list(string.ascii_letters + string.digits)

def generatePw(length):
    random.shuffle(characters)

    password = []
    for i in range(length):
        password.append(random.choice(characters))

    random.shuffle(password)

    result = "".join(password)
    return result

pw = generatePw(10)
username = input('Your username: ')

account = {
    'username': username,
    'password': pw
}

print(account)