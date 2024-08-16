#!/usr/bin/python3
"""
Log parsing module
"""
import sys

# 129.102.207.84 - [2024-08-15 11:17:23.534639] "GET /projects/260 HTTP/1.1" 403 896
# 103.103.37.244 - [2024-08-15 11:17:23.538151] "GET /projects/260 HTTP/1.1" 403 969
# 231.231.79.102 - [2024-08-15 11:17:23.657267] "GET /projects/260 HTTP/1.1" 401 145
# 166.51.143.15 - [2024-08-15 11:17:24.558030] "GET /projects/260 HTTP/1.1" 401 46
# 200, 301, 400, 401, 403, 404, 405 and 500
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
