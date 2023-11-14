#!/usr/bin/env python3

s = input()

while s != "end":
    tokens = s.split()
    if 1 < int(tokens[2]):
        print(s)
    s = input()
