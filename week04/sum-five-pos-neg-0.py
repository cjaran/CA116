#!/usr/bin/env python3

nt = 0
pt = 0

n = int(input())
while n != 0:
    if n < 0:
        nt = nt + n
    else:
        pt = pt + n
    n = int(input())

print(nt, pt)
