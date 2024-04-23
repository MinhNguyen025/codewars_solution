def rgb(r, g, b):
    # Ensure each input value is within the valid range of 0 to 255
    r = max(0, min(r, 255))
    g = max(0, min(g, 255))
    b = max(0, min(b, 255))

    # Convert each decimal value to its hexadecimal representation
    hex_r = hex(r)[2:].zfill(2)
    hex_g = hex(g)[2:].zfill(2)
    hex_b = hex(b)[2:].zfill(2)

    # Concatenate the hexadecimal representations of each color component
    return hex_r.upper() + hex_g.upper() + hex_b.upper()


# Test cases
print(rgb(255, 255, 255))  # "FFFFFF"
print(rgb(255, 255, 300))  # "FFFFFF"
print(rgb(0, 0, 0))  # "000000"
print(rgb(148, 0, 211))  # "9400D3"
