#!/usr/bin/env python3

import os

files = os.listdir(".")

i = 0
while i < len(files):
    file = files[i].split(".")
    print(file)
    backup_file = file[0] + "." + file[1] + ".bak"
    regular_file = ".".join(file)
    if not os.path.isfile(backup_file):
        with open(regular_file) as regular:
            t = regular.readline()
            while 0 < len(t):
                with open(backup_file, "w") as backup:
                    #backup.write(t.strip("\n"))
                    t = regular.readline()
    i += 1
