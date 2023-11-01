#!/usr/bin/env python3

s = input()

while s != "end":
    i = 0
    while i < len(s) and s[i] != ",":
        i = i + 1
    city = s[i - 4:i]
    full_city = s[:i]
    if city == "City" and len(city) < len(full_city):
        print(full_city)

    s = input()
