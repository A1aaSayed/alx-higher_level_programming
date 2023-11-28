#!/usr/bin/python3
for ch in range(24):
    if (ch + 97) == "e" or (ch + 97) == "q":
        continue
    print("{:s}".format(chr(ch + 97)), end='')
