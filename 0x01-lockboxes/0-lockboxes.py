#!/usr/bin/python3
""" lockboxes """


def canUnlockAll(boxes):
    """
    method that determines if all the boxes can be opened.

    boxes : list
        List of lists
    return: true|false
    """
    n = len(boxes)
    opened = set([0])
    closed = set(boxes[0]).difference(set([0]))
    while len(closed) > 0:
        box_index = closed.pop()
        if not box_index or box_index >= n or box_index < 0:
            continue
        if box_index not in opened:
            closed = closed.union(boxes[box_index])
            opened.add(box_index)
    return n == len(opened)
