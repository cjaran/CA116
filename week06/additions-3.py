#!/usr/bin/env python3

while sum != 1000:
    n = input()
    j = 0
    while j < len(n) and n[j] != "+":
        j = j + 1
    ls = n[:j]
    rs = n[j + 1:]
    sum = int(ls) + int(rs)
    print(sum)
