def palindrome(string):
    return "".join(string.split()).lower() == "".join(string[::-1].split()).lower()


def main():
    print(palindrome(input("Enter a string which can be a palindrome: ")))


if __name__ == '__main__':
    main()
