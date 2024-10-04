import sys

def read_numbers_from_file(filename):
    with open(filename, 'r') as file:
        return [int(line.strip()) for line in file]
def min_moves_to_make_equal(nums):
    nums.sort()
    n = len(nums)
    if n % 2 == 1:  
        median = nums[n // 2]
    else:  
        median = (nums[n // 2 - 1] + nums[n // 2]) / 2
    moves = sum(abs(num - median) for num in nums)
    return int(moves)
def main():
    if len(sys.argv) != 2:
        print("Использование: python script.py <имя_файла>")
        return
    filename = sys.argv[1]
    nums = read_numbers_from_file(filename)
    result = min_moves_to_make_equal(nums)
    print(result)
if __name__ == "__main__":
    main()
