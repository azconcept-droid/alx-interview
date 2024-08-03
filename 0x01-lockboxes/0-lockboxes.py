#!/usr/bin/python3
"""
This module open locked boxes
"""


def canUnlockAll(boxes):
    """ This method determines if all the boxes can be opened
    """

    # Number of boxes
    number_of_boxes = len(boxes)

    # first box is opened retreive the keys
    first_box = boxes[0]
    keys_at_hand = [initial_key for initial_key in first_box if initial_key < number_of_boxes]

    index = 0
    # Search for the keys
    while index < len(keys_at_hand):
        # Open the box and the retrieve keys
        # print("keys at hand = ", keys_at_hand)
        # print("boxes[{}] = ".format(keys_at_hand[index]), boxes[keys_at_hand[index]])
        for key in boxes[keys_at_hand[index]]:
            # if key is retreived twice skip
            if key not in keys_at_hand and key < number_of_boxes and key != 0:
                # print("key = ", key)
                keys_at_hand.append(key)
        index += 1

    # Check if all boxes have been opened indexing from 0
    if len(keys_at_hand) == number_of_boxes - 1:
        return True
    else:
        return False
