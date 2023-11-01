#!/usr/bin/env python3

s = input()

while s != "end":
    i = 0
    while i < len(s) and s[i] != ",":
        i = i + 1
    code = s[i + 1:i + 3]
    if code == "WI":
        print(s[:i])

    s = input()
