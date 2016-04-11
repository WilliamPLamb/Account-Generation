#! python3
# function file to create some number of accounts
# with random usernames and passwords

import shelve
from Generator import randomUsername, strongPassword

# print("Username:", randomUsername(8))
# print("Password:", strongPassword(20))

def createAccounts(usernameLength, passwordLength, size):
    shelfFile = shelve.open("accounts")
    for x in range(1, size):
        shelfFile["account" + str(x)] = [randomUsername(usernameLength), strongPassword(passwordLength)]
    shelfFile.close()