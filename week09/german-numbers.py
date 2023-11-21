#!/usr/bin/env python3

import sys

english = "zero one two three four five six seven eight nine ten".split()
german = "null eins zwei drei vier funf sechs sieben acht neun zehn".split()

translation = {}

i = 0
while i < len(english):
    translation[english[i]] = german[i]
    i = i + 1

word = sys.stdin.readline().rstrip()
while 0 < len(word):
    if word in english:
        print(translation[word])
    word = sys.stdin.readline().rstrip()
