#!/usr/bin/env python3

a = int(input())
b = int(input())

if a % 2 == 0 and (a // 2) == b:
    print("yes")
elif a % 2 != 0 and ((a * 3) + 1) == b:
    print("yes")
else:
    print("no")
