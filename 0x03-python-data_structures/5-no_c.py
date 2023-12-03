#!/usr/bin/python3
def no_c(my_string):
    char_list = [ch for ch in my_string]
    new_string = ''
    for ch in char_list:
        if ch != 'c' and ch != 'C':
            new_string += new_string.join(ch)
    return new_string
