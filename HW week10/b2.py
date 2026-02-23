def kth_largest(matrix, k):
    n = len(matrix)
    m = len(matrix[0])
    # chuyển về bài toán số nhỏ thứ t
    t = n * m - k + 1
    left = matrix[0][0]
    right = matrix[n - 1][m - 1]

    def count_le(x):
        count = 0
        i = n - 1
        j = 0
        while i >= 0 and j < m:
            if matrix[i][j] <= x:
                count += i + 1
                j += 1
            else:
                i -= 1
        return count

    while left < right:
        mid = (left + right) // 2
        if count_le(mid) >= t:
            right = mid
        else:
            left = mid + 1

    return left
matrix = [[1, 5, 9], 
          [10, 11, 13], 
          [12, 13, 15]]
print(kth_largest(matrix, 2))