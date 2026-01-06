import bisect
def maxSubarraySumModulo(nums, m):
    prefix = 0
    max_sum = 0
    sorted_prefix = [0]
    for num in nums:
        prefix = (prefix + num) % m

        # Case 1: subarray from start
        max_sum = max(max_sum, prefix)

        # Case 2: find smallest prefix > current prefix
        idx = bisect.bisect_right(sorted_prefix, prefix)
        if idx < len(sorted_prefix):
            candidate = (prefix - sorted_prefix[idx] + m) % m
            max_sum = max(max_sum, candidate)
        # insert prefix into sorted list
        bisect.insort(sorted_prefix, prefix)
    return max_sum