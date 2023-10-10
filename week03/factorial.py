#!/usr/bin/env python3

n = int(input())
total = 1

while 0 < n:
    total = total * n
    n = n - 1

print(total)
