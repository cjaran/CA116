#!/usr/bin/env python3

n = int(input())

if n % 2 * n != 0:
    print((n * 3) + 1)
elif (n + 1) % 2 * n != 0:
    print(n // 2)
