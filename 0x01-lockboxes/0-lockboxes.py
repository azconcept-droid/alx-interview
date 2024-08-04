#!/usr/bin/python3
"""
This module open locked boxes
"""


def canUnlockAll(boxes):
    """ This method determines if all the boxes can be opened
    """

    # Number of boxes
    number_of_boxes = len(boxes)

    # Get initial keys at hand starting from first box
    keys_at_hand = [0]

    # Starting to search from 1st key at hand
    index = 0
    # Search for the keys
    while index < len(keys_at_hand):
        # Open the box to retrieve the keys
        for key in boxes[keys_at_hand[index]]:
            # skip previously retreived keys & discard unwanted keys
            if key not in keys_at_hand and key < number_of_boxes:
                keys_at_hand.append(key)
        index += 1

    # Check if all boxes have been opened
    if len(keys_at_hand) == number_of_boxes:
        return True
    else:
        return False
