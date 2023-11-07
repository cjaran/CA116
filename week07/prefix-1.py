#!/usr/bin/env python3

if __name__ == "__main__":
    a = ["mountain", "montagne", "mont", "mo", "montages", "zebra", "monthly"]
    s = "mont"

i = 0
while i < len(a):
    t = a[i]
    if t[0:len(s)] == s:
        print(t)
    i = i + 1
