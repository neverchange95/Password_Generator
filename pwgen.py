import secrets
import string

""" This is a simple password generator which uses the python secrets module to generate strong random characters """
__author__ = "neverchange95"


def generate(length):
    # create a string with all digits, letters and punctuations
    characters = string.digits + string.ascii_letters + string.punctuation
    # create a string variable to save the password in it
    password = ""

    if length < 10:
        return "Your password is too short! It should have min 10 characters!"
    else:
        for i in range(length):
            # choose a random character from the "characters" variable "length" times
            password = password + secrets.choice(characters)
        return password


if __name__ == "__main__":
    # save the length input from user
    length = input("Please enter the length of your password, min. 10 characters!\n")

    # call generate() and cast the length variable to int
    print("Here is your password:\n" + generate(int(length)))
