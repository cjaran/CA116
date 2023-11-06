#!/usr/bin/env python3

s = input()
a = []

while s != "end":
    a.append(int(s))
    s = input()

location = 0
small = a[0]
i = 0
while i < len(a):
    if a[i] < small:
        location = i
        small = a[i]
    i = i + 1

print(location)
