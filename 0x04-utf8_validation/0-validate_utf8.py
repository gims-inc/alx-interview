#!/usr/bin/python3


def validUTF8(data):
    """Determines if a given data set represents a valid UTF-8 encoding.
    Args:
        data (list): The data set can contain multiple characters
    Returns:
        bool: True if data is a valid UTF-8 encoding,
              else return False.
    """
    i = 0
    while i < len(data):
        if (data[i] & 128) == 0:  # 1-byte sequence
            i += 1
        elif (data[i] & 224) == 192:  # 2-byte sequence
            if i + 1 >= len(data) or (data[i + 1] & 192) != 128:
                return False
            i += 2
        elif (data[i] & 240) == 224:  # 3-byte sequence
            for j in range(i + 1, i + 3):
                if i + 2 >= len(data) or (data[j] & 192) != 128:
                    return False
            i += 3
        elif (data[i] & 248) == 240:  # 4-byte sequence
            for j in range(i + 1, i + 4):
                if i + 3 >= len(data) or (data[j] & 192) != 128:
                    return False
            i += 4
        else:
            return False
    return True
