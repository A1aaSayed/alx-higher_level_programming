#!/usr/bin/python3
if __name__ == '__main__':
    from calculator_1 import add, sub, mul, div
    import sys
    args = sys.argv
    args_len = len(sys.argv) - 1

    if args_len != 3:
        print('Usage: ./100-my_calculator.py <a> <operator> <b>')
        exit(1)
    elif args[2] not in ['+', '-', '*', '/']:
        print('Unknown operator. Available operators: +, -, * and /')
        exit(1)
    else:
        if args[2] == '+':
            print('{} + {} = {}'
                  .format(args[1], args[3], add(args[1], args[3])))
        elif args[2] == '-':
            print('{} - {} = {}'
                  .format(args[1], args[3], sub(args[1], args[3])))
        elif args[2] == '*':
            print('{} * {} = {}'
                  .format(args[1], args[3], mul(args[1], args[3])))
        elif args[2] == '/':
            print('{} / {} = {}'
                  .format(args[1], args[3], div(args[1], args[3])))
