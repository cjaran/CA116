#!/usr/bin/env python3

import sys

args = sys.argv[1:]

total = 0

i = 0
while i < len(args):
    with open(args[i]) as f:
        s = f.readlines()
        j = 0
        while j < len(s):
            t = s[j].strip().split()
            k = 0
            while k < len(t):
                value = int(t[k])
                total = total + value
                k += 1
            j = j + 1
    i = i + 1

print(total)
