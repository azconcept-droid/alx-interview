#!/usr/bin/python3
"""
Log parsing module
"""
import sys

status_code_count = {
    '200': 0,
    '301': 0,
    '400': 0,
    '401': 0,
    '403': 0,
    '404': 0,
    '405': 0,
    '500': 0,
}

total_size = 0

count = 0
for line in sys.stdin:

    # print("File size: {}".format(total_size))
    if count == 10:
        print("File size: {}".format(total_size))
        count = 0
    for key in status_code_count.keys():
        # print(type(line.split(' ')[-2]), type(key))
        if line.split(' ')[-2] == key:
            status_code_count[key] += 1
            total_size += int(line.split(' ')[-1])
            print("{}: {}".format(key, status_code_count[key]))
    count += 1
