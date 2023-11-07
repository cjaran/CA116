#!/usr/bin/env python3

a = []
b = []

s = input()
while s != "end":
    a.append(int(s))
    s = input()

s = input()
while s != "end":
    b.append(int(s))
    s = input()

i = 0
j = 0
while i < len(a) and j < len(b):
    if a[i] < b[j]:
        print(a[i])
        i = i + 1
    else:
        print(b[j])
        j = j + 1

if len(a) != len(b):
    if len(a) < len(b):
        while j < len(b):
            print(b[j])
            j = j + 1
    elif len(b) < len(a):
        while i < len(a):
            print(a[i])
            i = i + 1
