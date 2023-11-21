#!/usr/bin/env python3

import sys

file = "translation.txt"

translation = {}

with open(file) as f:
    i = 0
    while i < len(file):
        t = f.readline().split()
        if t != []:
            translation[t[0]] = t[1]
        i = i + 1

s = sys.stdin.readline().rstrip()
while 0 < len(s):
    if s in translation:
        print(translation[s])
    s = sys.stdin.readline().rstrip()
