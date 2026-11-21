def rotate(nums, k):
    n = len(nums)
    k = k % n

    if k == 0:
        return

    temp = nums[n - k:]

    for i in range(n - k - 1, -1, -1):
        nums[i + k] = nums[i]

    for i in range(k):
        nums[i] = temp[i]


if __name__ == "__main__":
    nums = [1, 2, 3, 4, 5, 6, 7]
    rotate(nums, 3)
    print(nums)   # [5, 6, 7, 1, 2, 3, 4]

    nums = [-1, -100, 3, 99]
    rotate(nums, 2)
    print(nums) 