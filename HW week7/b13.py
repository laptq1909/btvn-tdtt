from collections import Counter
def longestHarmoniousSubsequence(arr):
    freq = Counter(arr)
    max_len = 0
    for x in freq:
        if x + 1 in freq:
            max_len = max(max_len, freq[x] + freq[x + 1])
    return max_len
print(longestHarmoniousSubsequence([1,3,2,2,5,2,3,7]))