#!/usr/bin/python3
"""Locked Boxes challenge"""


def canUnlockAll(boxes):
    """function that determines if all boxes are opened"""
    n = len(boxes)
    opened = [False] * n  # track opened boxes
    opened[0] = True  # first box is already opened
    keys = [0]  # begin with first box

    while keys:
        current = keys.pop()
        for key in boxes[current]:
            if key < n and not opened[key]:
                opened[key] = True
                keys.append(key)

    return all(opened)  # check if all boxes are opend
