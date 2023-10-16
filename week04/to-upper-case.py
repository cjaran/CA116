#!/usr/bin/env python3

s = input()
t = ""

i = 0
while i < len(s):
    x = ord(s[i])
    if x >= 97 and x <= 122:
        x = x - 32
    y = chr(x)
    t = t + y
    i = i + 1

print(t)
