#!/usr/bin/env python3

if __name__ == "__main__":
    a = ["cat", "elephant", "mouse", "lizard", "horse", "mongoose"]

i = 0
while i < len(a) and not (6 <= len(a[i])):
    i = i + 1

if i < len(a):
    print(a[i])
