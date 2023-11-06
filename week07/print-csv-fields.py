#!/usr/bin/env python3

s = input()
a = []

while s != "end":
    a.append(s)
    s = input()

n = int(input())

i = 0
while i < len(a):
    j = i
    line = a[i]
    while j < len(line) and line[j] != ",":
        j = j + 1
    if n == 0:
        print(line[:j])
    elif n == 1 or n == 2:
        k = j + 1
        while k < len(line) and line[k] != ",":
            k = k + 1
        if n == 1:
            print(line[j + 1:k])
        else:
            print(line[k + 1:])
    i = i + 1
