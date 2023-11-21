#!/usr/bin/env python3

import sys

s = sys.stdin.read()
print("\n".join(" ".join(s.split("\n")).split()))
