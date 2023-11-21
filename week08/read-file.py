#!/usr/bin/env python3

with open("input.txt") as f:
    s = f.readline()
    while 0 < len(s):
        print(s.strip("\n"))
        s = f.readline()
