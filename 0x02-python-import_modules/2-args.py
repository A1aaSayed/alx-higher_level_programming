#!/usr/bin/python3
import sys
args = sys.argv
args_len = len(sys.argv) - 1

if args_len == 0:
    print('0 arguments.')
elif args_len == 1:
    print('1 argument:')
    print('1: {:s}'.format(args[1]))
else:
    print('{} arguments:'.format(args_len))
    for i in range(1, args_len+1):
        print('{}: {:s}'.format(i, args[i]))
