#!/usr/bin/python3
import sys

if __name__ == "__main__":
    def add_up(*args):
        total = 0
        for i in args:
            total += i
        return total


args = sys.argv[1:]
args = [int(arg) for arg in args]
print(add_up(*args))
