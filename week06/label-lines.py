#!/usr/bin/env python3

s = input()

a = []
count = 0

while s != "end":
    count = count + 1
    a.append(s)
    s = input()

i = 0
while i < len(a):
    print(i, count, a[i])
    i = i + 1
