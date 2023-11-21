#!/usr/bin/env python3

filea = "a.txt"
fileb = "b.txt"

seena = {}
seenb = {}
printed = {}

with open(filea) as f:
    t = f.readlines()
    i = 0
    while i < len(t):
        if t[i] not in seena:
            seena[t[i]] = True
        i += 1

with open(fileb) as f:
    t = f.readlines()
    i = 0
    while i < len(t):
        if t[i] not in seenb:
            seenb[t[i]] = True
        i += 1

for item in seena:
    if item not in seenb and item not in printed:
        print(item.strip())
        printed[item] = True
