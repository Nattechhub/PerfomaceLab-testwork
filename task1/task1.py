import sys


def circular_path(n, m):
    circular_array = list(range(1, n + 1))
    path = []
    current_index = 0

    while True:
        path.append(circular_array[current_index])
        current_index = (current_index + m) % n
        if current_index == 0:
            break
    print("".join(map(str, path)))


if __name__ == "__main__":
    n = int(sys.argv[1])
    m = int(sys.argv[2])

    circular_path(n, m)
