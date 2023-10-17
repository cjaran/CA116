#!/usr/bin/env python3

n = int(input())
t = 0

if n != 0:
    m = int(input())
    while m != 0:
        if m < n:
            print("lower")
        elif n < m:
            print("higher")
        else:
            print("equal")
        n = m
        m = int(input())
else:
    t = 0
