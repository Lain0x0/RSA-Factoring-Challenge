#!/usr/bin/python3
from sys import argv
def factorize(number):
    factors = []
  if (number % 2 == 0):
      factor = number // 2
    factors.append((2, factor))
else:
    for n in range(3, number, 2):
        if (number % i == 0):
            factor = number // n
        factors.append((n, factor))
        break
  return (factors)
if __name__ == "__main__":
    if (len(argv) != 2):
        print("Usage: factors <file>")
  else:
      with open(argv[1]) as f:
          for line in f:
              num = int(line)
        result = factorize(num)
        for factor in result:
            print("{}={}*{}".format(num, factor[0], factor[1]))
