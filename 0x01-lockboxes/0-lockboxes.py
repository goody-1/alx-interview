#!/usr/bin/python3
"""The Lockboxes Project"""


def canUnlockAll(boxes):
    """Function to unlock boxes
    return: length of unlocked boxes
    """

    # Initialize a set to track unlocked boxes
    unlocked = set()
    # Start with the first box unlocked
    unlocked.add(0)
    # Initialize a stack for DFS
    stack = [0]

    while stack:
        # Get the current box number
        current_box = stack.pop()
        # Get keys from the current box
        for key in boxes[current_box]:
            # If the key opens a box that hasn't been unlocked yet
            if key not in unlocked and key < len(boxes):
                unlocked.add(key)  # Mark the box as unlocked
                # Add the box to the stack for further exploration
                stack.append(key)

    # If the number of unlocked boxes is equal to
    # the total number of boxes, return True
    return len(unlocked) == len(boxes)
