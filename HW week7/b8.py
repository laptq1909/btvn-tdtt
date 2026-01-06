import heapq
def minInterval(intervals, queries):
    # sort intervals by left endpoint
    intervals.sort(key=lambda x: x[0])
    # sort queries with original indices
    sorted_queries = sorted((q, i) for i, q in enumerate(queries))
    res = [-1] * len(queries)
    heap = []
    i = 0  # pointer for intervals
    for q, idx in sorted_queries:
        # add all intervals with l <= q
        while i < len(intervals) and intervals[i][0] <= q:
            l, r = intervals[i]
            length = r - l + 1
            heapq.heappush(heap, (length, r))
            i += 1
        # remove intervals that cannot cover q
        while heap and heap[0][1] < q:
            heapq.heappop(heap)
        # top of heap is smallest valid interval
        if heap:
            res[idx] = heap[0][0]
    return res