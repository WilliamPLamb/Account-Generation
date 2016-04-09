#! python3
# Gets account usernames and passwords from the stored file
# Usage: py.exe Acc.pyw

import shelve, pyperclip, sys

print("What brings you my way today, good user?")
print("account1 as default:")

# Open the data file
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