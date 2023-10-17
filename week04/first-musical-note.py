#!/usr/bin/env python3

s = input()
t = 0

i = 0
while i < len(s):
    if s[i] == "a" or s[i] == "b" or s[i] == "c" or s[i] == "d":
        print(s[i])
        i = len(s)
    elif s[i] == "e" or s[i] == "f" or s[i] == "g":
        print(s[i])
        i = len(s)
    else:
        i = i + 1
