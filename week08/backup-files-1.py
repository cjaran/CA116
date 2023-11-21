#!/usr/bin/env python3

import os

files = os.listdir(".")

i = 0
while i < len(files):
    file = files[i].split(".")
    if file[-1] != ".bak":
        backup = file[0] + "." + file[-1] + ".bak"
        with open(backup, "w") as f:
            with open(files[i]) as t:
                file_data = t.readline()
                j = 0
                while j < len(file_data):
                    f.write(file_data)
                    file_data = t.readline()
                    i += j
        i += 1
