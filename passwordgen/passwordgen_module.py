import string
import random


def passwordgen(lenght=8):
    chars = string.ascii_lowercase + string.ascii_uppercase + string.digits + string.punctuation
    return "".join([chars[random.randint(0, len(chars) - 1)] for index in range(lenght)])


def main():
    password_lenght = {"weak": 2, "medium": 4, "hard": 6, "strong": 8}
    print("How strong password do you want? Type one of these or enter a number:\n"
          "Weak (2 chars), Medium (4 chars), Hard (6 chars), Strong (8 chars)\n")
    lenght = input("Your choice: ")
    try:
        lenght = password_lenght[lenght.lower()]
    except:
        lenght = int(lenght)
    print("Your new password: {}".format(passwordgen(lenght)))


if __name__ == '__main__':
    main()
