#!/usr/bin/env python3

input_file = "irish-dobs.txt"
output_file = "american-dobs.txt"

with open(input_file) as f_in:
    with open(output_file, "w") as f_out:
        lines = f_in.readline()
        while 0 < len(lines):
            a = lines.split()
            date = a[0].split("/")
            day = lines.split()[0].split("/")[0]
            month = lines.split()[0].split("/")[1]
            date[0] = month
            date[1] = day
            new_date = "/".join(date)
            a[0] = new_date
            form_lines = " ".join(a)
            f_out.write(form_lines + "\n")
            lines = f_in.readline()
