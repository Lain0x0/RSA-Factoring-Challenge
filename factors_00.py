#!/usr/bin/python3
from sys import argv

with open(argv[1]) as f:
    for line in f:
        number = int(line)
        print("{:d}=".format(number), end="")
        if (number % 2 == 0):
            print("{}*2".format(number//2))
            continue
        for k in range(3, number, 2):
            if (number % k == 0):
                factor = number//k
                for j in range(3, factor, 2):
                    if (factor % j == 0 or k % j == 0):
                        break
                print("{}*{}".format(factor, k))
                break
