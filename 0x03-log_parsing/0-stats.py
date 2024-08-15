#!/usr/bin/python3
"""
Log parsing module
"""
import sys

# 129.102.207.84 - [2024-08-15 11:17:23.534639] "GET /projects/260 HTTP/1.1" 403 896
# 103.103.37.244 - [2024-08-15 11:17:23.538151] "GET /projects/260 HTTP/1.1" 403 969
# 231.231.79.102 - [2024-08-15 11:17:23.657267] "GET /projects/260 HTTP/1.1" 401 145
# 166.51.143.15 - [2024-08-15 11:17:24.558030] "GET /projects/260 HTTP/1.1" 401 46

count = 0
for line in sys.stdin:

    if count == 10:
        break
    for x in line.split(' '):
        print(x)
    count += 1
