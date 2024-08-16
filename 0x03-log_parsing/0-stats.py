#!/usr/bin/python3
"""
Log parsing module
"""
import sys

# Initialize status codes counts
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

# Initiliaze total size memory
total_size = 0

# Initialize lines count from 1
count_lines = 1

# Get each lines of the logs
for line in sys.stdin:
    # Iterate through the keys in the dictionary above
    for key in status_code_count.keys():
        # Extract the status code from the line of logs
        if line.split(' ')[-2] == key:
            # store the number of time the status codes occurs
            status_code_count[key] += 1
            # store the size of log
            total_size += int(line.split(' ')[-1])
    # Count the number of lines up to 10
    if count_lines % 10 == 0:
        # Print to stdout
        sys.stdout.write("File size: {}\n".format(total_size))
        for key, val in status_code_count.items():
            if val == 0:
                continue
            sys.stdout.write("{}: {}\n".format(key, val))
    count_lines += 1
