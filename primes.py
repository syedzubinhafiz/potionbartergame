import math


def largest_prime(k: int) -> int:
    # integer must be greater than 2
    if k <= 2:
        raise ValueError("k must be larger than 1!")
    a = []
    b = []

    # creates two lists: one contains boolean values of True
    # second one is all the number from integer 2 to k
    for i in range(2, k):
        a.append(True)
        b.append(i)

    # removes all the integers that can be divided by itself
    # including multiples of itself
    for i in range(len(a)):
        if a[i] is True:
            for j in range(i + 1, len(a)):
                if b[j] % b[i] == 0:
                    a[j] = False

    # traversing from the end of the list
    # gets the first integer that returns True from the back of the list
    for i in range(len(b) - 1, -1, -1):
        if a[i] is True:
            return b[i]


if __name__ == '__main__':
    print(largest_prime(1000))
