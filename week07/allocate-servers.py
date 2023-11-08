#!/usr/bin/env python3

s = input()
a = []
n = 0

while s != "end":
    a.append(int(s))
    current = 0

    i = 0
    while i < len(a):
        if int(s) <= a[i] + 1000:
            current += 1
            if n < current:
                n = current
        i = i + 1
    s = input()

print(n)
