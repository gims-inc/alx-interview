# UTF-8 Validation

Write a method that determines if a given data set represents a valid UTF-8 encoding.

    Prototype: def validUTF8(data)
    Return: True if data is a valid UTF-8 encoding, else return False
    A character in UTF-8 can be 1 to 4 bytes long
    The data set can contain multiple characters
    The data will be represented by a list of integers
    Each integer represents 1 byte of data, therefore you only need to handle the 8 least significant bits of each integer

        0x80 = 10000000: 1 byte character: 128
        0xC0 = 11000000: 2 byte character: 192
        0xE0 = 11100000: 3 byte character: 224
        0xF0 = 11110000: 4 byte character: 240

    check if the first byte is a valid UTF-8 character if it is, we check the next byte to see if it is a valid UTF-8 character
    in the case of a 3 byte character, we check the next 2 bytes

## Resources

 -[Bitwise --RealPython](https://realpython.com/python-bitwise-operators/)

 -[bitmasks --RealPython](https://realpython.com/python-bitwise-operators/#bitmasks)
