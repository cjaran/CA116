#!/usr/bin/env python3

small = 9999

i = 0
while i < 10:
    n = int(input())
    if 1 <= n:
        if n < small and n != 0:
            small = n
    i = i + 1

print(small)
