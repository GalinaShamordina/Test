import sys

def circular_array_path(n, m):
    if n <= 0:
        return "n должно быть положительным числом"
    if m <= 0:
        return "m должно быть положительным числом"
    circular_array = list(range(1, n + 1))
    path = []
    start_index = 0
    m = m % n
    if m == 0:
        return "m must be greater than 0"
    while True:
        end_index = (start_index + m - 1) % n
        path.append(circular_array[start_index])
        if end_index == 0:
            break
        start_index = end_index
    return ''.join(map(str, path))
if __name__ == "__main__":
    if len(sys.argv) != 3:
        print("Usage: python script.py n m")
        sys.exit(1)
    n = int(sys.argv[1])
    m = int(sys.argv[2])
    result = circular_array_path(n, m)
    print(result)

