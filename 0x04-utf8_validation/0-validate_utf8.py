#!/usr/bin/python3
"""
UTF-8 validation implementation
A character in UTF-8 can be 1 to 4 bytes long
The data set can contain multiple characters
The data will be represented by a list of integers
Each integer represents 1 byte of data, therefore you only need
    to handle the 8 least significant bits of each integer
"""


def validUTF8(data):
    """
    Determines if a given data set represents a valid UTF-8 encoding.
    Args:
        data (list): The data set can contain multiple characters
    Returns:
        bool: True if data is a valid UTF-8 encoding,
              else return False.
    """
    i = 0
    while i < len(data):
        if (data[i] & 128) == 0:
            i += 1
        elif (data[i] & 224) == 192:
            if i + 1 >= len(data) or (data[i + 1] & 192) != 128:
                return False
            i += 2
        elif (data[i] & 240) == 224:
            for j in range(i + 1, i + 3):
                if i + 2 >= len(data) or (data[j] & 192) != 128:
                    return False
            i += 3
        elif (data[i] & 248) == 240:
            for j in range(i + 1, i + 4):
                if i + 3 >= len(data) or (data[j] & 192) != 128:
                    return False
            i += 4
        else:
            return False
    return True
