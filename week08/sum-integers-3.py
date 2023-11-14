#!/usr/bin/env python3

import sys

args = sys.argv[1:]

total = 0

i = 0
while i < len(args):
    with open(args[i]) as f:
        t = f.readlines()
        j = 0
        while j < len(t):
            total = total + int(t[j])
            j += 1
    i = i + 1

print(total)
