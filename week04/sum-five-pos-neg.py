#!/usr/bin/env python3

nt = 0
pt = 0

i = 0
while i < 5:
    n = int(input())
    if n < 0:
        nt = nt + n
    else:
        pt = pt + n
    i = i + 1

print(nt, pt)
