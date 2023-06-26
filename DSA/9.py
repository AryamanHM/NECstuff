import struct

def little_to_big_endian(little_endian):
    # Unpack the little-endian value using struct
    unpacked_value = struct.unpack("<I", little_endian)[0]

    # Convert the value to big-endian using struct
    big_endian = struct.pack(">I", unpacked_value)

    return big_endian

# Test the program
little_endian_value = b"\x01\x00\x00\x00"

big_endian_value = little_to_big_endian(little_endian_value)

print("Little-Endian:", little_endian_value.hex())
print("Big-Endian:", big_endian_value.hex())
