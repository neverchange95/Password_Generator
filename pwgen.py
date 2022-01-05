import secrets
import string

""" This is a simple password generator which uses the python secrets module to generate strong random characters """
__author__ = "neverchange95"


def generate(length):
    # create a string with all digits, letters and punctuations
    characters = string.digits + string.ascii_letters + string.punctuation
    # create a string variable to save the password in it
    password = ""

    for i in range(length):
        # choose a random character from the "characters" variable "length" times
        password = password + secrets.choice(characters)

    return password


if __name__ == "__main__":
    # save the length input from user
    length = input("Please enter the length of your password, min. 10 characters!\n")

    checkInput = False

    while not checkInput:
        if not length.isdigit():
            print("You have to enter a digit!")
            length = input()
        else:
            if int(length) < 10:
                print("Enter min. 10!")
                length = input()
            else:
                checkInput = True

    running = True
    password = ""

    # generate a new password with min 1 digit, 1 character and 1 punctuation
    while running:
        password = generate(int(length))

        number = False
        character = False
        punctuation = False

        for i in range(0, len(password)):
            if password[i] in string.digits:
                number = True
            if password[i] in string.punctuation:
                punctuation = True
            if password[i] in string.ascii_letters:
                character = True


        if not number or not punctuation or not character:
            running = True
        else:
            running = False

    # call generate() and cast the length variable to int
    print("Here is your password:\n\n" + password)
