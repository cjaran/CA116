#!/usr/bin/env python3

import sys

s = sys.stdin.readline().rstrip()
a = []

while 0 < len(s):
    a.append(s)
    s = sys.stdin.readline().rstrip()

i = 0
while i < len(a):
    t = a[i]
    s = t.split("/")
    print(s[-1])
    i += 1
