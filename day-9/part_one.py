from functools import reduce
from itertools import repeat

# input_disk_map = '2333133121414131402'
input_disk_map = open('input').read()

def create_block_representation(disk_map: str) -> list[str]:
    blocks: list[str] = []

    for idx, char in enumerate(disk_map):
        if idx % 2 == 0:
            file_id = str(int(idx/2))
            blocks.extend(repeat(file_id, int(char)))
        else:
            blocks.extend(repeat('.', int(char)))

    return blocks

def reorganize_blocks(blocks: list[str]):
    reorganized_block_list = []

    for block in blocks:
        if block == '.':
            while (_block := blocks.pop()) == '.': pass
            reorganized_block_list.append(_block)
        else:
            reorganized_block_list.append(block)

    reorganized_block_list.extend(repeat('.', len(blocks)-len(reorganized_block_list)))
    return reorganized_block_list

def calc_checksum(blocks: list[str]) -> int:
    return reduce(lambda checksum, iv: checksum + (iv[0]*int(block) if (block := iv[1]) != '.' else 0), enumerate(blocks), 0)

if __name__ == "__main__":
    blocks = create_block_representation(input_disk_map)
    reorganized_blocks = reorganize_blocks(blocks)

    checksum = calc_checksum(reorganized_blocks)

    print('Checksum? ', checksum)
