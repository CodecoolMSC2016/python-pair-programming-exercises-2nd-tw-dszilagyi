import random


def listoverlap(list1, list2):
    return list(filter(lambda number: number in list1, list2))


def main():
    print(listoverlap([random.randint(0, 1000) for index in range(random.randint(0, 1000))],
                      [random.randint(0, 1000) for index in range(random.randint(0, 1000))]))

if __name__ == '__main__':
    main()
