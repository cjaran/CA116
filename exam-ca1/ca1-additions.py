#!/usr/bin/env python3

s = input()

while s != "end":
    i = 0
    while i < len(s) and s[i] != " ":
        i = i + 1

    lc = s[:i]
    rc = s[i + 1:]
    ls = lc + " + " + rc
    total = int(lc) + int(rc)
    t = " " * (21 - len(ls) - 2) + ls + " = " + str(total)
    print(t)
    s = input()
