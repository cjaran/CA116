#!/usr/bin/env python3

n = int(input())
m = int(input())

i = 0

print(m)
while i < (n - 1):
    if m % 2 * m != 0:
        m = ((m * 3) + 1)
        print(m)
    elif (m + 1) % 2 * m != 0:
        m = (m // 2)
        print(m)
    i = i + 1
