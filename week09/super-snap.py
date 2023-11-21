#!/usr/bin/env python3

import sys

s = sys.stdin.readline().rstrip()
seen = {}

while 0 < len(s) and s not in seen:
    seen[s] = True
    s = sys.stdin.readline().rstrip()

if 0 < len(s):
    print("snap: " + s)
