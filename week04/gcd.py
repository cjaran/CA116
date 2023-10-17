#!/usr/bin/env python3

a = int(input())
b = int(input())
oa = 0
ob = 0

i = 0
while b != 0:
    ob = b
    oa = a
    b = oa % ob
    a = b
    i = i + 1

print(i)
