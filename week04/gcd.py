#!/usr/bin/env python3

a = int(input())
b = int(input())
r = a % b

while r != 0:
    a = b
    b = r
    r = a % b

print(b)
