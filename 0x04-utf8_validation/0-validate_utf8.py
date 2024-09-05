#!/usr/bin/python3
""" UTF-8 Validation """

def validUTF8(data):
    # Number of bytes in the current UTF-8 character
    num_bytes = 0
    
    # Masks to check the significant bits
    mask1 = 1 << 7  # 10000000
    mask2 = 1 << 6  # 01000000

    for num in data:
        # Get the 8 least significant bits
        byte = num & 0xFF
        
        if num_bytes == 0:
            # Determine the number of bytes in this UTF-8 character
            mask = 1 << 7
            while mask & byte:
                num_bytes += 1
                mask >>= 1

            # 1-byte character
            if num_bytes == 0:
                continue

            # Invalid UTF-8 character
            if num_bytes == 1 or num_bytes > 4:
                return False
        else:
            # Check that the byte starts with "10"
            if not (byte & mask1 and not (byte & mask2)):
                return False

        num_bytes -= 1

    return num_bytes == 0
