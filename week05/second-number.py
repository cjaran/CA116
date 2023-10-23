#!/usr/bin/env python3

s = input()
#s = "abc 188 efg 911 abc 123"

i = 0
while i < len(s) and not ("0" <= s[i] and s[i] <= "9"):
    i = i + 1

if i < len(s):
    j = i
    while j < len(s) and "0" <= s[j] and s[j] <= "9":
        j = j + 1

    k = j
    while k < len(s) and not ("0" <= s[k] and s[k] <= "9"):
        k = k + 1

    ii = k
    while ii < len(s) and "0" <= s[ii] and s[ii] <= "9":
        ii = ii + 1

    print(s[k:ii], k)
