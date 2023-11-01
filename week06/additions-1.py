#!/usr/bin/env python3

i = 0
while i < 10:
    n = input()
    j = 0
    while j < len(n) and n[j] != "+":
        j = j + 1
    ls = n[:j]
    rs = n[j + 1:]
    print(int(ls) + int(rs))
    i = i + 1
