def canJump(nums):
    farthest = 0
    for i in range(len(nums)):
        if i > farthest:
            return False
        farthest = max(farthest, i + nums[i])
        if farthest >= len(nums) - 1:
            return True
    return True


if __name__ == "__main__":
    print(canJump([0]))                 # True
    print(canJump([2, 0, 0]))           # True
    print(canJump([3, 2, 1, 0, 4]))     # False
   