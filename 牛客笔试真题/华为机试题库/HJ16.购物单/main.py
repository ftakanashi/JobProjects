

def process(prices, values, affi, N):
    m = len(prices)
    dp = [[0 for _ in range(N // 10 + 1)] for _ in range(m + 1)]
    for i in range(1, m+1):
        p = prices[i-1] // 10
        v = values[i-1]
        for j in range(1, N//10 + 1):
            if j < p or i not in affi:    # 当前钱不够或者物品是附件
                dp[i][j] = dp[i-1][j]
            else:
                dp[i][j] = max(dp[i-1][j-p]+v, dp[i-1][j])
                if len(affi[i]) > 0:
                    i1 = affi[i][0]
                    p1, v1 = prices[i1-1] // 10, values[i1-1]    # 别忘了p进入DP数组计算都要除以10
                    if j >= p+p1: dp[i][j] = max(dp[i-1][j-p-p1]+v+v1, dp[i][j])
                    if len(affi[i]) == 2:
                        i2 = affi[i][1]
                        p2, v2 = prices[i2-1] // 10, values[i2-1]
                        if j >= p+p2: dp[i][j] = max(dp[i-1][j-p-p2]+v+v2, dp[i][j])
                        if j >= p+p1+p2: dp[i][j] = max(dp[i-1][j-p-p1-p2]+v+v1+v2, dp[i][j])

    print(dp[-1][-1])

def main():
    N, m = map(int, input().strip().split())
    prices, values, parents = [], [], []
    affi = {}
    for i in range(m):
        price, value, parent = map(int, input().strip().split())
        if parent > 0:
            if parent not in affi: affi[parent] = []
            affi[parent].append(i+1)
        else:
            affi[i+1] = []
        prices.append(price)
        values.append(value * price)

    process(prices, values, affi, N)

main()