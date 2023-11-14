#!/usr/bin/env python3

s = input()

while s != "end":
    tokens = s.split()
    if int(tokens[1][0]) == 0:
        temp = tokens[1][1:]
        tokens[1] = str(temp)
    start = tokens[1] + ":00"
    if int(tokens[2]) == 1:
        end = tokens[1] + ":50"
    elif int(tokens[2]) == 2:
        time = int(tokens[1]) + 1
        end = str(time) + ":50"
    elif int(tokens[2]) == 3:
        time = int(tokens[1]) + 2
        end = str(time) + ":50"
    tokens[2] = end
    tokens[1] = start
    print(" ".join(tokens))
    s = input()
