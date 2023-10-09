#!/usr/bin/env python3

weight = int(input())
height = int(input())

bmi = weight / (height * height) * 10000

if 30 <= bmi:
    print("obese")
elif 25 <= bmi:
    print("overweight")
elif 18.5 <= bmi:
    print("normal")
else:
    print("underweight")
