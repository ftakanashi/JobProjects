import sys

def process(s, costs):
    n = len(s)
    dp = [[0 for _ in range(n)] for _ in range(n)]

    for l in range(1, n):
        for i in range(n):
            j = i + l
            if j >= n: break
            if s[i] == s[j]:
                dp[i][j] = dp[i+1][j-1]
            else:
                cands = []
                cands.append(dp[i+1][j] + min(costs[s[i]]))
                cands.append(dp[i][j-1] + min(costs[s[j]]))
                cands.append(dp[i+1][j-1] + min(costs[s[i]][0] + costs[s[j]][1],
                                                costs[s[i]][1] + costs[s[j]][0]))
                dp[i][j] = min(cands)

    return dp[0][-1]

def main():
    s = sys.stdin.read().strip()
    # s = '12322'
    costs = {
        '1': (100, 120),
        '2': (200, 350),
        '3': (360, 200),
        '4': (220, 320)
    }
    res = process(s, costs)
    print(res)

main()