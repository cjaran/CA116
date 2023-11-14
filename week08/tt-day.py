#!/usr/bin/env python3

s = input()
a = []

while s != "end":
    tokens = s.split()
    a.append(tokens)
    s = input()

day = int(input())

i = 0
while i < len(a):
    if day == int(a[i][0]):
        print(" ".join(a[i]))
    i += 1
