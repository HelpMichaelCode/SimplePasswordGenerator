# Importing packages to generate random passwords
import random
import string


def complexPassword():
    # The complex password will include lowercase letters, digits, punctuation, and at least one uppercase letter.
    characters = string.ascii_lowercase + string.digits + string.punctuation
    password = [random.choice(characters) for _ in range(11)]

    password.append(random.choice(string.ascii_uppercase))

    random.shuffle(password)
    password = ''.join(password)

    print("Generated Complex Password:", password)

def simplePassword():
    # The simple password will include lowercase letters and digits, and at least one uppercase letter.
    characters = string.ascii_lowercase + string.digits
    password =  [random.choice(characters) for _ in range(11)]

    password.append(random.choice(string.ascii_uppercase))

    random.shuffle(password)
    password = ''.join(password)

    print("Generated Simple Password:", password)

# Main program
print("Welcome to the password generator!\nPlease select an option: \n[1] Complex Password\n[2] Simple Password")
choice = input("Enter your choice: ")

# Validate user input
while choice not in ['1', '2']:
    print("Invalid choice. Please select either [1] or [2].")
    choice = input("Enter your choice: ")

if choice == '1':
    print("You have selected Complex Password. Please select look at the options below to set your complex password:")
    complexPassword()
elif choice == '2':
    print("You have selected Simple Password. Please see the generated password below:")
    simplePassword()