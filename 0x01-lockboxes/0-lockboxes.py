#!/usr/bin/python3
"""
This module open locked boxes
"""


def canUnlockAll(boxes):
    """ This method determines if all the boxes can be opened
    """

    # Number of boxes
    number_of_boxes = len(boxes)

    # Save retrieved keys
    extracted_keys = {0}

    # first box is opened retreive the keys
    first_box = boxes[0]
    for initial_key in first_box:
        extracted_keys.add(initial_key)

    index = 1
    # Search for the keys
    while index < len(extracted_keys):
        # Open the box and the retrieve keys
        for key in boxes[index]:
            # if key is retreived twice skip
            if key not in extracted_keys:
                extracted_keys.add(key)
        index += 1

    # Check if all boxes have been opened
    if len(extracted_keys) == number_of_boxes:
        return True
    else:
        return False
