#!/usr/bin/python3
"""
This module open locked boxes
"""


def canUnlockAll(boxes):
    """ This method determines if all the boxes can be opened
    """

    # Number of boxes
    number_of_boxes = len(boxes)

    # Since first box is always open only one box is true
    if number_of_boxes == 1:
        return True

    # first box is opened retreive the keys
    # first_box = boxes[0]

    # Get initial keys at hand starting from first box
    keys_at_hand = [0]
    # for initial_key in first_box:
    #     if initial_key < number_of_boxes:
    #         keys_at_hand.append(initial_key)

    index = 0
    # Search for the keys
    while index < len(keys_at_hand):
        # Open the box and the retrieve keys
        for key in boxes[keys_at_hand[index]]:
            # if key is retreived twice skip
            if key not in keys_at_hand and key < number_of_boxes:
                keys_at_hand.append(key)
        index += 1

    # Check if all boxes have been opened indexing from 0
    # print("keys = ", keys_at_hand)
    # print("total keys = ", len(keys_at_hand))
    # print("Boxes = ", number_of_boxes)
    if len(keys_at_hand) == number_of_boxes:
        return True
    else:
        return False
