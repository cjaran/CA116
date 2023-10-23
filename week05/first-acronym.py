#!/usr/bin/env python3

s = input()
#s = "call the FBI, Skippy"

i = 0
while i < len(s) and not("A" <= s[i] and s[i] <= "Z"):
    i = i + 1

if i < len(s):
    j = i
    while j < len(s) and "A" <= s[j] and s[j] <= "Z":
        j = j + 1

    print(s[i:j], i)
