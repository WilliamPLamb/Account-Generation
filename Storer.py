#! python3
# My class names are too long

import shelve
from Generator import random_username, strong_password

print("Username:", random_username(8))
print("Password:", strong_password(30))

shelfFile = shelve.open("accounts")
for x in range(1, 501):
    shelfFile["account" + str(x)] = [random_username(8), strong_password(30)]
shelfFile.close()