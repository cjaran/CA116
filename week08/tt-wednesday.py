#!/usr/bin/env python3

s = input()

while s != "end":
    tokens = s.split()
    if int(tokens[0]) == 3:
        print(s)
    s = input()
