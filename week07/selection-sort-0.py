#!/usr/bin/env python3

s = input()
smallest = int(s)

while s != "end":
    if int(s) < smallest:
        smallest = int(s)
    s = input()

print(smallest)
