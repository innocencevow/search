def dailyTemperatures(temperatures):
    n = len(temperatures)
    answer = [0] * n
    stack = []

    for i in range(n):
        while stack and temperatures[i] > temperatures[stack[-1]]:
            j = stack.pop()
            answer[j] = i - j
        stack.append(i)

    return answer


if __name__ == "__main__":

    print(dailyTemperatures([30, 40, 50, 60]))
    # [1, 1, 1, 0]

    print(dailyTemperatures([30, 60, 90]))
    # [1, 1, 0]