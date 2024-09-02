#!/usr/bin/env python3
"""
This module contains a function to validate if a given dataset represents
a valid UTF-8 encoding.
"""

from typing import List

def validUTF8(data: List[int]) -> bool:
    """
    Determine if a given dataset represents a valid UTF-8 encoding.

    Args:
        data (List[int]): A list of integers where each integer represents 1 byte.

    Returns:
        bool: True if data is a valid UTF-8 encoding, else False.
    """
    # Number of bytes in the current UTF-8 character
    n_bytes = 0

    # Masks to check the most significant bits
    mask1 = 1 << 7  # 10000000
    mask2 = 1 << 6  # 01000000

    for num in data:
        # Get the binary representation of the number, taking only the last 8 bits
        bin_rep = num & 0xFF

        if n_bytes == 0:
            # Count the number of leading 1s to determine the number of bytes in the character
            mask = 1 << 7
            while mask & bin_rep:
                n_bytes += 1
                mask = mask >> 1

            # 1-byte character or 0 leading 1s (valid case)
            if n_bytes == 0:
                continue

            # If the number of bytes is more than 4 or 1 (invalid cases)
            if n_bytes == 1 or n_bytes > 4:
                return False
        else:
            # Check if the most significant bits are '10'
            if not (bin_rep & mask1 and not (bin_rep & mask2)):
                return False
        
        # Decrease the number of bytes to process
        n_bytes -= 1

    # If there are no remaining bytes to process, the data is valid UTF-8
    return n_bytes == 0