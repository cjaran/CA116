#!/usr/bin/env python3

import sys

file = sys.argv[1]
s = sys.argv[2:]

with open(file, "w") as f:
    i = 0
    while i < len(s):
        f.write(s[i] + "\n")
        i = i + 1
