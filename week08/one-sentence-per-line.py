#!/usr/bin/env python3

s = input()
t = ""

while s != "end":
    t = t + " " + s
    s = input()

t = " ".join(t.split()).split(".")

i = 0
while i < len(t):
    if len(t[i]) > 0:
        if t[i][0] == " ":
            t[i] = t[i][1:]
    if t[i] != "":
        print(t[i] + ".")
    i = i + 1
