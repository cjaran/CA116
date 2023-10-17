#!/usr/bin/env python3

s = input()
total = 0

i = 0
while i < len(s):
    total = total + int(s[len(s) - 1 - i]) * 2 ** i
    i = i + 1

print(total)
