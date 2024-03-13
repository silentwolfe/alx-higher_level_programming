#!/usr/bin/python3

a = 65
z = 90

while z >= a:
  if (z % 2 == 0):
    print(chr(z + 32), end="")
  else:
    print(chr(z), end="")
  z = z - 1
