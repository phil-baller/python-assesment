def calculate_storage(filesize):
    block_size = 4096
    full_blocks = filesize // block_size
    partial_block_remainder = filesize % block_size
    if partial_block_remainder > 0:
        return (full_blocks + 1) * block_size
    return filesize

print(calculate_storage(1))
print(calculate_storage(4096))
print(calculate_storage(4097))
print(calculate_storage(6000))