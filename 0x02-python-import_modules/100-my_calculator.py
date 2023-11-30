#!/usr/bin/python3
if __name__ == '__main__':
    from calculator_1 import add, sub, mul, div
    import sys
    args = sys.argv
    args_len = len(sys.argv) - 1

    if args_len != 3:
        print('Usage: ./100-my_calculator.py <a> <operator> <b>')
        exit(1)
    a = args[1]
    b = args[3]
    ope = args[2]
    if ope == '+':
        print('{} {} {} = {}'
                .format(a, ope, b, add(a, b)))
    elif ope == '-':
        print('{} {} {} = {}'
                .format(a, ope, b, sub(a, b)))
    elif ope == '*':
        print('{} {} {} = {}'
                .format(a, ope, b, mul(a, b)))
    elif ope == '/':
        print('{} {} {} = {}'
                .format(a, ope, b, div(a, b)))
    else:
        print('Unknown operator. Available operators: +, -, * and /')
        exit(1)
