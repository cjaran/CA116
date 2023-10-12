#!/usr/bin/env python3

n = int(input())
#n = 30

i = 2
while i < n:
    candidate_prime = i
    j = 2
    divisors = 0
    while j < i:
        if canidate_prime % j == 0 and divisors == 0:
            divisors = divisors + 1
    if divisors == 0:
        print(candidate_prime)
        j = j + 1
    i = i + 1
