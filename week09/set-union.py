#!/usr/bin/env python3

filea = "a.txt"
fileb = "b.txt"

seen = {}

with open(filea) as f:
    t = f.readlines()
    i = 0
    while i < len(t):
        if t[i] not in seen:
            seen[t[i]] = "Value"
        i = i + 1

with open(fileb) as f:
    t = f.readlines()
    i = 0
    while i < len(t):
        if t[i] not in seen:
            seen[t[i]] = "Value"
        i = i + 1

for i in seen:
    print(i.strip())
