#!/usr/bin/env python3

import os

files = os.listdir(".")

i = 0
while i < len(files):
    s = files[i].split(".")
    if s[-1] == "py":
        with open(files[i]) as f:
            check = f.readline(1)
            if check != "":
                print(files[i])
    i += 1
