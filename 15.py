def searchRange(nums, target):
    def find_left():
        left = 0
        right = len(nums) - 1
        pos = -1
        while left <= right:
            mid = (left + right) // 2
            if nums[mid] == target:
                pos = mid
                right = mid - 1
            elif nums[mid] < target:
                left = mid + 1
            else:
                right = mid - 1
        return pos

    def find_right():
        left = 0
        right = len(nums) - 1
        pos = -1
        while left <= right:
            mid = (left + right) // 2
            if nums[mid] == target:
                pos = mid
                left = mid + 1
            elif nums[mid] < target:
                left = mid + 1
            else:
                right = mid - 1
        return pos

    return [find_left(), find_right()]


if __name__ == "__main__":
    print(searchRange([5, 7, 7, 8, 8, 10], 8))   # [3, 4]
    print(searchRange([5, 7, 7, 8, 8, 10], 6))   # [-1, -1]
    print(searchRange([], 0))                     # [-1, -1]
    