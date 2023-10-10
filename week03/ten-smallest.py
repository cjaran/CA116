#!/usr/bin/env python3

small = 9999

i = 0
while i < 10:
    n = int(input())
    if n < small:
        small = n
    i = i + 1

print(small)
