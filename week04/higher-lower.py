#!/usr/bin/env python3

n = int(input())

i = 0
while i < 5:
    m = int(input())
    if m < n:
        print("lower")
    elif n < m:
        print("higher")
    else:
        print("equal")
    n = m
    i = i + 1
