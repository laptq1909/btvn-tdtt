def xuli(nums):
    a, b, c, d, e = nums[0], nums[1], nums[2], nums[3], nums[4]
    ans = 0
    if a > b: a, b = b, a 
    if c > d: c, d = d, c 
    if d > b:
        if c > e: c, e = e, c 
        if e > b:
            if b > c: ans = b
            else: ans = c 
        else:
            if e > a: ans = e
            else: ans = a
    else:
        if a > e: a, e = e, a
        if e > d:
            if d > a: ans = d
            else: ans = a
        else:
            if e > c: ans = e
            else: ans = c
    return ans

nums = list(map(int, input().split()))
print(xuli(nums))