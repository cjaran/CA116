#!/usr/bin/env python3

import sys

file = sys.argv[1]

with open(file, "w") as f:
    f.write("Hello world.\n")
