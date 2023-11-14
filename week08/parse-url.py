#!/usr/bin/env python3

import sys

args = sys.argv[1]

tokens = args.split("/")

print("scheme:", tokens[0][0:-1])
i = 0
while i < len(tokens[2]) and tokens[2][i] != ":":
    i += 1
print("host:", tokens[2][:i])
if i < len(tokens[2]) and tokens[2][i + 1] != "":
    print("port:", tokens[2][i + 1:])

i = 0
while i < len(tokens[3]) and tokens[3][i] != "?":
    i = i + 1
print("path:", "/" + tokens[3][:i])
j = i + 1
while i < len(tokens[3]) and tokens[3][i] != "#":
    i = i + 1
if i <= len(tokens[3]):
    print("query-string:", tokens[3][j:i])
if i < len(tokens[3]):
    print("fragment-id:", tokens[3][i + 1:])
