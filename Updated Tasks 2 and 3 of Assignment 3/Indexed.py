def indexed_file_allocation():
    total_blocks = int(input("Enter total number of blocks: "))
    block_status = [0] * total_blocks

    n = int(input("Enter number of files: "))
    for i in range(n):
        index = int(input(f"Enter index block for file {i+1}: "))
        if index < 0 or index >= total_blocks:
            print("Invalid index block.")
            continue
        if block_status[index] == 1:
            print("Index block already allocated.")
            continue
        count = int(input(f"Enter number of data blocks for file {i+1}: "))
        data_blocks = list(map(int, input(f"Enter {count} data block numbers separated by space: ").split()))
        if len(data_blocks) != count or any(blk < 0 or blk >= total_blocks for blk in data_blocks):
            print("Invalid data blocks input.")
            continue
        if any(block_status[blk] == 1 for blk in data_blocks):
            print("One or more data blocks already allocated.")
            continue
        block_status[index] = 1
        for blk in data_blocks:
            block_status[blk] = 1
        print(f"File {i+1} allocated with index block {index} -> {data_blocks}")

if __name__ == "__main__":
    indexed_file_allocation()
