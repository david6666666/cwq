def maxLoss(prices):
    r = 0
    for i in range(1, len(prices)):
        v = prices[i] - prices[i - 1]
        r += v if v < 0 else 0
    return r



arr = list(map(int,input().split(',')))
print(abs(maxLoss(arr)))