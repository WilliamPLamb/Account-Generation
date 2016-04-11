#! python3
# Gets account usernames and passwords from the stored file
# and generates a new set if they do not already exist
# To get a fresh set of accounts, delete the accounts.db file
# and run Acc.py again.

# For Account generation (account.db file)
usernameLength = 8
passwordLength = 20
size = 101

import shelve, pyperclip, os
from Storer import createAccounts

print("What brings you my way today, good user?")
print("account1 as default:")

# Generate data file accounts.db if DNE
if not os.path.exists("accounts.db"):
    createAccounts(usernameLength, passwordLength, size)
# open data file
accountShelf = shelve.open("accounts")


# Get data for first account to display
username, password = accountShelf["account1"]
print("Username: ", username)
print("Password: ", password)

while(True):
    print("If you want any other account,")
    print("Use format \"account<int>\" <\"Username\" or \"Password\">")
    print("Example: \"account1 username\"")
    print("Or type quit to finish")
    desired = input()
    if desired.lower() == "quit":
        break
    # Incorrect Input
    if len(desired.split()) != 2:
        print("Incorrect parameters")
        continue
    # Get parameters
    accountNum, option = desired.split()
    # Get desired account
    try:
        username, password = accountShelf[accountNum]
    except KeyError:
        print("Accounts range from 1 to 100")
        continue
    # Print Account Username and Password
    print(accountNum + ":")
    print("Username: ",username)
    print("Password: ", password)
    # Copies desired parameter to the clipboard
    if option.lower() == "username":
        print("Username copied.")
        pyperclip.copy(username)
    elif option.lower() == "password":
        print("Password copied.")
        pyperclip.copy(password)
    #Didn't write parameters correctly
    else:
        print("Invalid second parameter")

print("Program exiting")
accountShelf.close()