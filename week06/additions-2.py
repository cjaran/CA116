#!/usr/bin/env python3

s = input()
total = 0

i = 0
while i < len(s):
    j = i
    while j < len(s) and s[j] != "+":
        j = j + 1
    num = int(s[i:j])
    total = total + num
    i = j + 1

print(total)
