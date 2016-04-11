#! python3
# generates passwords and usernames randomly

import random
import string

# print string.punctuation
# remove indices 1,6,29 ?


def strongPassword(length):
    password_list = []
    password = ''
    for x in range(length):
        password_list.append(string.ascii_letters[random.randint(0,51)])
    for x in range(length):
        password_list.append(string.digits[random.randint(0,9)])
    for x in range(length):
        password_list.append(string.punctuation[random.randint(0,31)])
    for x in range(length):
        password = password + ''.join(password_list[random.randint(0,len(password_list) - 1)])
    return password

# returns random username of upper case letter,
# the rest of the username is letters, except for the
# last four digits
# length should be at least 5
def randomUsername(length):
    username = ''
    username = username + string.ascii_uppercase[random.randint(0,25)]
    for x in range(length - 5):
        username = username + string.ascii_lowercase[random.randint(0,25)]
    for x in range(4):
        username = username + str(random.randint(0,9))
    return username

# print("Username:", random_username(10))
# print("Password:", strong_password(30))