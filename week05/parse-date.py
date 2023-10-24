#!/usr/bin/env python3

#s = "Tuesday 23rd October, 2018"
s = input()

i = 0
while i < len(s) and s[i] != " ":
    i = i + 1

day = s[:i]
day = "(" + day + ")"

j = i + 1
while j < len(s) and s[j] != " ":
    j = j + 1
date = s[i + 1:j]
date = date + ","

k = j + 1
while k < len(s) and s[k] != " ":
    k = k + 1
month = s[j + 1:k - 1]

ii = k + 2
while ii < len(s) and s[ii] != " ":
    ii = ii + 1
year = s[k + 1:ii]

print(month, date, year, day)
