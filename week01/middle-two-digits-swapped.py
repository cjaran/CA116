#!/usr/bin/env python3

n = int(input())
n = n % 10000
n = int(n // 100)

a = n // 10
b = n % 10

print((b * 10) + a)
