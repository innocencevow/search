def longestConsecutive(nums):
    num_set = set(nums)

    best = 0

    for x in num_set:
        if x - 1 in num_set:
            continue
        cur = x        
        length = 1
        while cur + 1 in num_set:
            cur += 1
            length += 1
        if length > best:
            best = length

    return best


if __name__ == "__main__":
    print(longestConsecutive([]))   # 0
    print(longestConsecutive([1, 2, 0, 1]))   # 3