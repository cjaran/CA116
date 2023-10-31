#!/usr/bin/env python3

n = input()

a = []

while n != "end":
    a.append(int(n))
    n = input()

m = int(input())

i = 0
while i < len(a):
    print(a[i] + m)
    i = i + 1
