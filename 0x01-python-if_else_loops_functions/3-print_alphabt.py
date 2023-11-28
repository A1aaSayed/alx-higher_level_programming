#!/usr/bin/python3
for ch in range(ord('a'), ord('z') + 1):
    if chr(ch) not in ['q', 'e']:
        print(f'{chr(ch)}', end='')
