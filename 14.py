def combinationSum(candidates, target):
    candidates.sort()
    result = []
    path = []

    def backtrack(i, remain):
        if remain == 0:
            result.append(path[:])
            return
        if i == len(candidates) or remain < 0:
            return

        path.append(candidates[i])
        backtrack(i, remain - candidates[i])
        path.pop()

        backtrack(i + 1, remain)

    backtrack(0, target)
    return result


if __name__ == "__main__":
    print(combinationSum([2, 3, 6, 7], 7))   # [[2, 2, 3], [7]]
    print(combinationSum([2, 3, 5], 8))      # [[2, 2, 2, 2], [2, 3, 3], [3, 5]]