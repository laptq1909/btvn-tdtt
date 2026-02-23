def findRadius(houses, heaters):
    ans = 0
    for house in houses:
        l = 0
        r = len(heaters) - 1
        while l < r:
            m = (l + r) // 2
            if heaters[m] < house:
                l = m + 1
            else: r = m
        dist = abs(house - heaters[l])
        if l > 0:
            dist = min(dist, abs(house - heaters[l - 1]))
        ans = max(ans, dist)
    return ans

houses = list(map(int, input().split()))
heaters = list(map(int, input().split()))
houses = sorted(houses)
heaters = sorted(heaters)
print(findRadius(houses, heaters))