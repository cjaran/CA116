#!/usr/bin/env python3

import os

files = os.listdir(".")

i = 0
while i < len(files):
    s = files[i].split(".")
    if s[-1] == "py":
        print(files[i])
    else:
        with open(files[i]) as f:
            check = f.read()
            if 0 < len(check) and check[0] == "#!/usr/bin/env python3\n":
                print(files[i])
    i += 1
