#!/usr/bin/python3
if __name__ == '__main__':
    import sys
    args = sys.argv
    args_len = len(sys.argv) - 1
    sum = 0
    for i in range(1, args_len + 1):
        sum += int(args[i])
    print(sum)
