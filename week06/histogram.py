#!/usr/bin/env python3

s = input()
a = []
h = []

while s != "end":
    n = int(s)
    a.append(n)
    s = input()

i = 0
while i < len(a):
    j = 0
    while j < len(a) and j <= 9:
        count = 0
        if a[i] == j:
            count = count + 1
        add = a[i] + count
        h.append(add)
        j = j + 1
    i = i + 1

print(h)
