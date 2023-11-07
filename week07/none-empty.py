#!/usr/bin/env python3

count = 0

i = 0
while i < len(a):
    if len(a[i]) != 0:
        count = count + 1
    i = i + 1

print(count)
