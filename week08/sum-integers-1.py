#!/usr/bin/env python3

import sys

a = sys.stdin.readline()
total = 0

while a != "" and int(a) != 0:
    total = total + int(a)
    a = sys.stdin.readline()

print(total)
