#!/usr/bin/env python3

import sys

s = sys.stdin.readline().split(".")
eof = s[1]
files = {}

while 0 < len(s):
    files[s[0].strip()] = s[-1].strip()
    s = sys.stdin.readline()
    if s != "":
        s = s.split(".")

for i in files:
    t = files.get(i, "correct")
    if t == "correct":
        print(i + "." + eof)
