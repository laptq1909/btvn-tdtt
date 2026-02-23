def canPlaceFlowers(flowerbed, k):
    if len(flowerbed) == 1:
        return flowerbed[0] == 0 and k == 1
    tmp = 0
    for i in range(len(flowerbed)):
        if i == 0:
            if flowerbed[i] + flowerbed[i + 1] == 0:
                flowerbed[i] = 1
                tmp += 1
        elif i == len(flowerbed) - 1:
            if flowerbed[i] + flowerbed[i - 1] == 0:
                flowerbed[i] = 1
                tmp += 1
        else:
            if flowerbed[i] + flowerbed[i - 1] + flowerbed[i + 1] == 0:
                flowerbed[i] = 1
                tmp += 1
    return tmp == k

li = list(map(int, input().split()))
k = int(input())
print(canPlaceFlowers(li, k))