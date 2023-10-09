#!/usr/bin/env python3

x = int(input())
y = int(input())
z = int(input())

x_y_z = (x * x + y * y) == z * z
y_z_x = (y * y + z * z) == x * x
z_x_y = (z * z + x * x) == y * y

print(x_y_z or y_z_x or z_x_y)
