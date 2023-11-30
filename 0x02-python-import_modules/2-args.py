#!/usr/bin/python3
if __name__ == '__main__':
    import sys
    args = sys.argv
    args_len = len(sys.argv) - 1

    if args_len == 0:
        print('{} arguments.'.format(0))
    elif args_len == 1:
        print('{} argument:'.format(1))
        print('{}: {:s}'.format(1, args[1]))
    else:
        print('{} arguments:'.format(args_len))
        for i in range(1, args_len + 1):
            print('{}: {:s}'.format(i, args[i]))
