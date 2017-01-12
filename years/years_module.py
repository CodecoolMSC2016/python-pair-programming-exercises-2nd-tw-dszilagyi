import datetime


def years(age):
    return datetime.date.today().year - int(age) + 99


def main():
    name = input("Please enter your name: ")
    age = int(input("Please enter your age: "))
    for index in range(int(input("Please enter a number how may times you want to get the message: "))):
        print("{}, you will turn 100 years old in: {}".format(name, years(age)))


if __name__ == '__main__':
    main()
