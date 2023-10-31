#!/usr/bin/env python3

n = input()

odd = []
even = []

while n != "end":
    if int(n) % 2 == 0:
        even.append(int(n))
    else:
        odd.append(int(n))
    n = input()

i = 0
while i < len(even):
    print(even[i])
    i = i + 1

i = 0
while i < len(odd):
    print(odd[i])
    i = i + 1
