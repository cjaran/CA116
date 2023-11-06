#!/usr/bin/env python3

s = input()
a = []

while s != "end":
    a.append(int(s))
    s = input()

i = int(input())

location = i
small = a[i]
j = i
while j < len(a):
    if a[j] < small:
        location = j
        small = a[j]
    j += 1

print(location)
