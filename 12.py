from collections import deque


def canFinish(numCourses, prerequisites):
    graph = []
    for i in range(numCourses):
        graph.append([])

    in_degree = [0] * numCourses

    for pair in prerequisites:
        a = pair[0]
        b = pair[1]
        graph[b].append(a)
        in_degree[a] += 1

    queue = deque()
    for i in range(numCourses):
        if in_degree[i] == 0:
            queue.append(i)

    finished = 0

    while queue:
        course = queue.popleft()
        finished += 1

        for nxt in graph[course]:
            in_degree[nxt] -= 1
            if in_degree[nxt] == 0:
                queue.append(nxt)

    return finished == numCourses


if __name__ == "__main__":
    print(canFinish(2, [[1, 0]]))                    # T
    print(canFinish(2, [[1, 0], [0, 1]]))            # F