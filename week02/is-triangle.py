#!/usr/bin/env python3

x = int(input())
y = int(input())
z = int(input())

if (x + y) <= z or (x + z) <= y or (y + z) <= x:
    print("no")
else:
    print("yes")
