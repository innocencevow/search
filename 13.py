def subsets(nums):
    result = []
    path = []

    def backtrack(i):
        if i == len(nums):
            result.append(path[:])
            return

        path.append(nums[i])
        backtrack(i + 1)
        path.pop()

        backtrack(i + 1)

    backtrack(0)
    return result


if __name__ == "__main__":
    print(subsets([1, 2, 3]))
    
    print(subsets([0]))
    # [[0], []]