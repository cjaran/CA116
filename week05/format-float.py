#!/usr/bin/env python3

s = input()

i = 0
while i < len(s):
    if i == 0 and s[i] == ".":
        print("0" + s)

    if s[i] == s[len(s) - i -1]:
        print(s + ".0")
    i = i + 1

    if i == 0 and s[i] == "-":
        j = 0
        while j < len(s) and s[j] != ".":
            j = j + 1
        if j < len(s):
            print(s + ".0")
if i == len(s):
    print(s)
