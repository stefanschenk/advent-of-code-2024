from itertools import groupby, repeat, chain

from part_one import create_block_representation, calc_checksum

# input_disk_map = '2333133121414131402'
input_disk_map = open('input').read()

def index_blocks(blocks: list[str]):
    last_block_idx = 0
    indexed_blocks = dict()

    for k,g in groupby(blocks):
        g = list(g)
        blockIdx = blocks.index(g[0], last_block_idx)
        indexed_blocks.update({blockIdx:g})
        last_block_idx = blockIdx + len(g)

    return indexed_blocks

def reorganize_files(blocks: dict[int, list[str]]):
    res = dict(reversed(list(blocks.items())))
    ordered_blocks = blocks.copy()

    def combine_and_sort(items):
        # dict is ordered by insert, so sort after inserting a new space
        sortedItems = sorted(items)
        spaces = []

        for idx, item in enumerate(sortedItems):
            if any(el == '.' for el in item[1]):
                spaces.append(idx)

        last_space_idx = -1
        while spaces:
            if (space_idx := spaces.pop()) == last_space_idx - 1:
                [_, source] = sortedItems.pop(last_space_idx)
                [_, target] = sortedItems[space_idx]

                target.extend(source)

            last_space_idx = space_idx

        return dict(sortedItems)


    for k,v in res.items():
        is_file = not(any(el == '.' for el in v))

        if is_file:
            for l,w in ordered_blocks.items():
                is_space = any(el == '.' for el in w) and l<k
                if is_space and (spaceSize := len(w)) >= (fileSize := len(v)):
                    ordered_blocks.update({l: v}) # add file to space
                    ordered_blocks[k] = list(repeat('.', fileSize)) # convert file to space

                    # update space to decrease it's size
                    if fileSize < spaceSize:
                        ordered_blocks[l+fileSize] = list(repeat('.', spaceSize-fileSize))
                        ordered_blocks = dict(combine_and_sort(ordered_blocks.items()))

                    break

    return list(chain.from_iterable(ordered_blocks.values()))


if __name__ == "__main__":
    blocks = create_block_representation(input_disk_map)
    indexed_blocks = index_blocks(blocks)
    reorganized_blocks = reorganize_files(indexed_blocks)

    checksum = calc_checksum(reorganized_blocks)

    print('Checksum? ', checksum)
