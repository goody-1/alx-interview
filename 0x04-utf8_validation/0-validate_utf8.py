#!/usr/bin/python3
"""Module to validate a utf-8 encoding"""


def validUTF8(data):
    # Number of bytes remaining in the current UTF-8 character
    bytes_remaining = 0

    # Loop through each integer in the data
    for num in data:
        # Get the 8 least significant bits of each integer (last byte)
        byte = num & 0xFF

        # If bytes_remaining is 0, we are expecting a new character
        if bytes_remaining == 0:
            # Determine how many bytes the character spans
            if (byte >> 5) == 0b110:
                bytes_remaining = 1  # 2-byte character
            elif (byte >> 4) == 0b1110:
                bytes_remaining = 2  # 3-byte character
            elif (byte >> 3) == 0b11110:
                bytes_remaining = 3  # 4-byte character
            elif (byte >> 7) != 0:  # 1-byte character (ASCII range)
                return False
        else:
            # If we're in the middle of a character,
            # it must start with 10xxxxxx
            if (byte >> 6) != 0b10:
                return False
            bytes_remaining -= 1

    # All characters should be complete, so bytes_remaining should be 0
    return bytes_remaining == 0
