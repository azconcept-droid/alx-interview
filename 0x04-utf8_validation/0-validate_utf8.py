#!/usr/bin/python3
""" utf-8 validation module
"""


def validUTF8(data):
    """ this method validate if a data is a valid utf-8 encoding"""

    # Initialize number of bytes to be 0 - 1-byte
    num_of_bytes = 0

    # Iterate through each character byte in the data
    for byte in data:
        # convert to 8-bits binary
        binary = format(byte, '08b')

        # Determine the number of bytes in utf-8
        if num_of_bytes == 0:
            # 1-byte
            if binary[0] == '0':
                continue
            # 2-byte
            elif binary[:3] == '110':
                num_of_bytes = 1
            # 3-byte
            elif binary[:4] == '1110':
                num_of_bytes = 2
            # 4-byte
            elif binary[:5] == '11110':
                num_of_bytes = 3
            else:
                return False
        else:
            # check if the following bytes start with '10'
            if binary[:2] != '10':
                return False
            num_of_bytes -= 1

    return True
