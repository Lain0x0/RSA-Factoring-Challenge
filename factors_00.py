# #usr/bin/python3
import sys

with open(argv[1]) as file_rsa:
    for line in file_rsa:
        number = int(line)
        print("{:d}=".format(number), end="")
        if (number % 2 == 0):
            print("{}*2".format(number//2))
            continue
        for i in range(3, number, 2):
            if (number % i == 0):
                factor = number//i
                for j in range(3, factor, 2):
                    if (factor % j == 0 or i % j == 0):
                        break
                print("{}*{}".format(factor, i))
                break
