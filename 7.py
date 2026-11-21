def maxSubArray(nums):
    cur = 0
    best = nums[0]   
    for x in nums:
        cur = cur + x

        if cur > best:
            best = cur
        if cur < 0:
            cur = 0

    return best


if __name__ == "__main__":
    print(maxSubArray([-2, 1, -3, 4, -1, 2, 1, -5, 4]))   # 6
    print(maxSubArray([1]))        # 1
    print(maxSubArray([-1]))       # -1
    