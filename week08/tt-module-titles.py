#!/usr/bin/env python3

s = input()

while s != "end":
    tokens = s.split()
    t = tokens[5:]
    print(" ".join(t))
    s = input()
