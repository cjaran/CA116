#!/usr/bin/env python3

big = 0

i = 0
while i < 10:
    n = int(input())
    if big < n:
        big = n
    i = i + 1

print(big)
