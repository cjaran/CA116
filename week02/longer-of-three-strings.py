#!/usr/bin/env python3

s1 = input()
s2 = input()
s3 = input()

s1_t = len(s1) > len(s2) and len(s1) > len(s3)
s2_t = len(s2) > len(s1) and len(s2) > len(s3)
s3_t = len(s3) > len(s2) and len(s3) > len(s1)

if s1_t:
    print(s1)
elif s2_t:
    print(s2)
elif s3_t:
    print(s3)
