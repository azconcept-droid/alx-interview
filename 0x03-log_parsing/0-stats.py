#!/usr/bin/python3
"""
Log parsing module
"""
import sys
import re
import signal

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


def print_stats(total_size, status_code_count):
    """ Print statistics """
    # Print to stdout
    print("File size: {}".format(total_size))
    for key, val in status_code_count.items():
        if val == 0:
            continue
        print("{}: {}".format(key, val))


def signal_handler(sig, frame):
    """ Signal handler """
    if sig == 2:
        print_stats(total_size, status_code_count)


# Register the signal handler for SIGINT
signal.signal(signal.SIGINT, signal_handler)

# Pattern to check
# The pattern to match
pattern = regex = r"^\d.*\s\-\s\[\d*.*\]\s\"GET.*\"\s(\d*)\s(\d*)$"
# pattern = r'^\d{1,3}\.\d{1,3}\.\d{1,3}\.\d{1,3} - \[\d{4}-\d{2}-\d{2}
#  \d{2}:\d{2}:\d{2}\.\d{6}\] "GET /projects/\d+ HTTP/1\.1" \d{3} \d+$'
# Get each lines of the logs
for line in sys.stdin:
    # Check the pattern
    # Check if the line matches the pattern
    match = re.match(pattern, line)
    # if line did not match skip
    if match is None:
        continue
    # Iterate through the keys in the dictionary above
    for key in status_code_count.keys():
        # Extract the status code from the line of logs
        if line.split(' ')[-2] == key:
            # store the number of time the status codes occurs
            status_code_count[key] += 1
            # store the size of log
            total_size += int(line.split(' ')[-1])
    # Count the number of lines up to 10 then repeat printing
    if count_lines % 10 == 0:
        # Print to stdout
        print_stats(total_size, status_code_count)
    count_lines += 1
