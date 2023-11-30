#!/usr/bin/python3
def uppercase(str):
    new_str = ''
    for ch in str:
        if 'a' <= ch <= 'z':
            uppercase_ch = chr(ord(ch) - 32)
            new_str += uppercase_ch
        else:
            new_str += ch
    print('{}'.format(new_str))
