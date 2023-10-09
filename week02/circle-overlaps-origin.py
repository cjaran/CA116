#!/usr/bin/env python3

x = int(input())
y = int(input())
r = int(input())

dist_to_origin = ((x * x) + (y * y)) ** 0.5

print(dist_to_origin < r)
