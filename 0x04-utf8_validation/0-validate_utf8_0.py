#!/usr/bin/python3


def validUTF8(data):
    """Determines if a given data set represents a valid UTF-8 encoding.
    Args:
        data (list): The data set can contain multiple characters
    Returns:
        bool: True if data is a valid UTF-8 encoding,
              else return False.
    """
    valid = 0
    for value in data:
        byte = value & 255
        if valid:
            if byte >> 6 != 2:
                return False
            valid -= 1
            continue
        while (1 << abs(7 - valid)) & byte:
            valid += 1
        if valid == 1 or valid > 4:
            return False
        valid = max(valid - 1, 0)
    return valid == 0

data = [65]
print(validUTF8(data))

data = [80, 121, 116, 104, 111, 110, 32, 105, 115, 32, 99, 111, 111, 108, 33]
print(validUTF8(data))

data = [229, 65, 127, 256]
print(validUTF8(data))

data = [250, 145, 145, 145, 145]
print  (validUTF8(data))

data = [0, 0, 0, 0, 0, 0]
print  (validUTF8(data))

data = [467, 133, 108]
print  (validUTF8(data))

data = [240, 188, 128, 167]
print  (validUTF8(data))