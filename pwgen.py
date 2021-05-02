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

    # call generate() and cast the length variable to int
    print("Here is your password:\n\n" + generate(int(length)))
