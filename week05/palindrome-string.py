#!/usr/bin/env python3

s = input()
#s = "rotator"

i = 0
while i < len(s) and s[i] == s[len(s) - i - 1]:
    i = i + 1

if i >= len(s):
    print("palindrome")
