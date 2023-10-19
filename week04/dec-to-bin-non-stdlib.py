#!/usr/bin/env python3

n = int(input())
base = 2
output = ""

while n != 0:
    output = str(n % base) + output
    n = n // base

print(output)
