#!/usr/bin/python3

def canUnlockAll(boxes):
    """
    Determines if all boxes can be opened.
    :param boxes: List of lists, where each list contains keys to other boxes.
    :return: True if all boxes can be opened, False otherwise.
    """
    if not isinstance(boxes, list) or len(boxes) == 0:
        return False
    
    n = len(boxes)
    opened = set([0])  # Start with the first box opened
    keys = list(boxes[0])  # Start with keys from the first box

    while keys:
        key = keys.pop()
        if key < n and key not in opened:
            opened.add(key)
            keys.extend(boxes[key])  # Add keys from the newly opened box
    
    return len(opened) == n
