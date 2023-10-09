#!/usr/bin/env python3

n = int(input())

i = 0

while i < n:
    i = i + 1
    if i % 5 == 0 and i % 3 == 0:
        print("fizz-buzz")
    elif i % 3 == 0:
        print("fizz")
    elif i % 5 == 0:
        print("buzz")
    else:
        print(i)
