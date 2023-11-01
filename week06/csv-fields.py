#!/usr/bin/env python3

s = input()

i = 0
while i < len(s):
    j = i
    while j < len(s) and s[j] != ",":
        j = j + 1
    print(s[i:j])
    i = j + 1
