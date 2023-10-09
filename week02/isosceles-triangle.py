#!/usr/bin/env python3

n1 = int(input())
n2 = int(input())
n3 = int(input())

isosceles = (n1 == n2) or (n2 == n3) or (n1 == n3)

print(isosceles)
