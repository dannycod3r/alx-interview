#!/usr/bin/python3
"""
Supplies a function to validate UTF-8
"""


def validUTF8(data):
    # Number of bytes in the current UTF-8 character
    num_bytes = 0

    # Masks to identify the most significant bits (MSBs)
    mask1 = 1 << 7    # 10000000
    mask2 = 1 << 6    # 01000000

    # Iterate over each integer in the data list
    for num in data:
        # Get the 8 least significant bits (last 8 bits)
        byte = num & 0xFF
        # If num_bytes is 0, we are checking for a new UTF-8 character
        if num_bytes == 0:
            # Determine the number of bytes for the character
            if (byte & mask1) == 0:
                # 1-byte character (0xxxxxxx)
                continue
            elif (byte & (mask1 >> 1)) == 0:
                return False
            else:
                # Count the leading 1s to determine the number of bytes
                while (byte & mask1):
                    num_bytes += 1
                    byte <<= 1
                # UTF-8 characters can only be 1 to 4 bytes long
                if num_bytes == 1 or num_bytes > 4:
                    return False
        else:
            # Continuation byte (should start with 10xxxxxx)
            if not (byte & mask1 and not (byte & mask2)):
                return False

        # We processed one byte, so decrement the count
        num_bytes -= 1

    # If num_bytes is not 0, then we have an incomplete UTF-8 character
    return num_bytes == 0
