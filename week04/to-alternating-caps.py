#!/usr/bin/env python3

s = input()
t = ""
n = 0

i = 0
while i < len(s):
    x = ord(s[i])
    if x >= 97 and x <= 122:
        x = x - 32
    y = chr(x)
    if n % 2 != 0 and s[i] != " " and i != 0:
        t = t + y
    else:
        t = t + s[i]
    n = n + 1
    i = i + 1

print(t)
