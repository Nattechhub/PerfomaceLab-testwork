import sys


def min_moves_to_equal(nums):
    if not nums:
        return 0

    target = sum(nums) // len(nums)
    moves = 0

    for num in nums:
        moves += abs(num - target)

    return moves


if __name__ == "__main__":
    if len(sys.argv) < 2:
        print("Используй команду: task4.py input.txt")
        sys.exit(1)

    input_file = sys.argv[1]

    with open(input_file, 'r') as file:
        nums = [int(line.strip()) for line in file.readlines()]

    min_moves = min_moves_to_equal(nums)
    print(min_moves)
