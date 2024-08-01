#!/usr/bin/python3
"""
This module open locked boxes
"""


def canUnlockAll(boxes):
    """ This method determines if all the boxes can be opened
    """

    # Store opened boxes here, first box is opened
    extracted_keys = {0}
    current_boxes = []
    unlocked_boxes = []
    first_box = boxes[0]

    # 1 iteration
    # Open first box
    current_boxes.append(first_box)

    # print("Extracted keys = ", extracted_keys)
    # print(boxes)
    # print("opened boxes = ", current_boxes)

    # Extract the keys in first box
    for key in first_box:
        # save the opened boxes
        extracted_keys.add(key)
        current_boxes.append(boxes[key])

    # print("visited boxes = ", extracted_keys)
    # print(boxes)
    # print("opened boxes = ", current_boxes)

    # 2
    # Open the new boxes using the extracted keys
    # to get new keys
    new_keys = {}
    new_keys = {keys for box in current_boxes for keys in box}

    # print("new keys = ", new_keys)

    # Extract the keys in new opened boxes
    current_boxes = []
    for key in new_keys:
        extracted_keys.add(key)
        current_boxes.append(boxes[key])

    # print("visited boxes = ", extracted_keys)
    # print(boxes)
    # print("opened boxes = ", current_boxes)

    # 3
    # Open the new boxes using the extracted keys
    # to get new keys
    new_keys = {}
    new_keys = {keys for box in current_boxes for keys in box}

    # print("new keys = ", new_keys)

    # Extract the keys in new opened boxes
    current_boxes = []
    for key in new_keys:
        extracted_keys.add(key)
        current_boxes.append(boxes[key])

    # print("visited boxes = ", extracted_keys)
    # # print(boxes)
    # print("opened boxes = ", current_boxes)

        # 3
    # Open the new boxes using the extracted keys
    # to get new keys
    new_keys = {}
    new_keys = {keys for box in current_boxes for keys in box}

    # print("new keys = ", new_keys)

    # Extract the keys in new opened boxes
    current_boxes = []
    for key in new_keys:
        extracted_keys.add(key)
        current_boxes.append(boxes[key])

    unlocked_boxes = [boxes[key] for key in extracted_keys]

    # print("unlocked boxes", unlocked_boxes)
    # print("boxes", boxes)
    if unlocked_boxes == boxes:
        return True

    return False
    # last_key = new_keys - extracted_keys
