#!/usr/bin/env python3

n = int(input())
base = 16
output = ""

digits = "0123456789abcdef"

while n != 0:
    print(digits[n % base])
    n = n // base

print(output)
