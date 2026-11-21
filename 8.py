def merge(intervals):
    # 先按起点从小到大排序
    intervals.sort(key=lambda x: x[0])

    result = []
    cur_start = intervals[0][0]
    cur_end = intervals[0][1]

    for i in range(1, len(intervals)):
        start = intervals[i][0]
        end = intervals[i][1]

       
        if start <= cur_end:
            if end > cur_end:
                cur_end = end
        else:
            
            result.append([cur_start, cur_end])
           
            cur_start = start
            cur_end = end
    result.append([cur_start, cur_end])

    return result

if __name__ == "__main__":
    cases = [
        ([[1,3],[2,6],[8,10]], [[1,6],[8,10]]),
        ([[1,2],[3,4],[5,6]], [[1,2],[3,4],[5,6]]),
        ([[8,10],[1,3],[2,6]], [[1,6],[8,10]]),
        ([[1,4],[4,5]], [[1,5]]),
        ([[1,10],[2,3],[4,5]], [[1,10]]),
        ([[1,4],[1,5]], [[1,5]]),
        ([[1,1],[1,1]], [[1,1]]),
        ([[-5,-3],[-2,0],[0,3]], [[-5,-3],[-2,3]]),
        ([[5,7]], [[5,7]]),
    ]
    for i, (inp, want) in enumerate(cases, 1):
        got = merge(inp)
        print(f"#{i}", "✅" if got == want else f"❌ 期望 {want} 实际 {got}")