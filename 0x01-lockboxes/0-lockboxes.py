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
    # print("first extracted keys = ", extracted_keys)
    # print("number of keys = ", number_of_boxes)
 
    index = 1
    # Search for the keys
    # boxes = [[1], [2], [3], [4], []]
    # boxes = [[1, 4, 6], [2], [0, 4, 1], [5, 6, 2], [3], [4, 1], [6]]
    # boxes = [[1, 4], [2], [0, 4, 1], [3], [], [4, 1], [5, 6]]

    while index < len(extracted_keys):
        # print("index = ", index)
        # print("boxes[{}] = ".format(index), boxes[index])
        # Open the box and the retrieve keys
        for key in boxes[index]:
            # print("key = ", key)
            if key not in extracted_keys:
                extracted_keys.add(key)
                # print("Extracted keys =", extracted_keys)
        index += 1

    # print(len(extracted_keys))
    # print(number_of_boxes)

    if len(extracted_keys) == number_of_boxes:
        return True
    else:
        return False

# canUnlockAll([[1, 4, 6], [2], [0, 4, 1], [5, 6, 2], [3], [4, 1], [6]])

# canUnlockAll([[1], [2], [3], [4], []])
    # # 1 iteration
    # # Open first box
    # current_boxes.append(first_box)

    # index = 0
    # while index < number_of_boxes:
    #     # Open the new boxes using the extracted keys
    #     # to get new keys
    #     # Extract the keys in new opened boxes
    #     set_of_keys = boxes[keys]
    #     new_keys = {keys for box in current_boxes for keys in box}
    #     for key in new_keys:
    #         extracted_keys.add(key)
    #         current_boxes.append(boxes[key])

    #     print("visited boxes = ", extracted_keys)
    #     print("opened boxes = ", current_boxes)
    #     print("new keys = ", new_keys)
    #     new_keys = {}
    #     current_boxes = []

    #     index += 1

    # unlocked_boxes = [boxes[key] for key in extracted_keys]

    # # All boxes are unlocked return true
    # if unlocked_boxes == boxes:
    #     return True
    

    # print("unlocked boxes", unlocked_boxes)
    # print("boxes", boxes)
    # return False
    # # last_key = new_keys - extracted_keys
