#!/usr/bin/python3

for z in range(ord('Z'), ord('A') - 1, -1):
    print('{0}'.format(chr(z + 32) if z % 2 == 0 else chr(z)), end="")
