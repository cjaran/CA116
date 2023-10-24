#!/usr/bin/env python3

n = int(input())

t = ""
s = ""
base = 16

digits = "0123456789abcdef"

while n != 0:
    t = t + digits[n % base]
    n = n // base

j = 0
while j < len(t):
    s = s + t[len(t) - j - 1]
    j = j + 1

i = 0
while i < len(s) and not("a" <= s[i] and s[i] <= "f"):
    i = i + 1

if i < len(s):
    print(s[i])
