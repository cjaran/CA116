#!/usr/bin/env python3

numbers = []

i = 0
n = input()
while n != "end":
    count = 0
    numbers.append([i, count])

    if int(n) <= i:
        numbers[int(n)][1] = numbers[int(n)][1] + 1
        n = input()
    i = i + 1

i = 0
while i < len(numbers):
    if 0 < numbers[i][1]:
        print(str(numbers[i][0]))
        numbers[i][1] = numbers[i][1] - 1
        i = i - 1
    i = i + 1
