#!/usr/bin/env python3

n = int(input())
p = int(input())

digit = n % (10 ** (p + 1))
digit = digit // (10 ** p)

print(digit)
