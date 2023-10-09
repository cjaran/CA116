#!/usr/bin/env python3

mark = int(input())

print("first:", mark >= 70)
print("second:", mark >= 50 and mark <= 69)
print("third:", mark >= 40 and mark <= 49)
print("fail:", mark <= 39)
