from typing import List

def getMaxMatrix(matrix: List[List[int]]) -> List[int]:

    def getStartEnd(nums):
        dp = ans = nums[0]
        ans_end, ans_start = 0, 0
        for i in range(1, len(nums)):
            if dp + nums[i] < nums[i]:
                dp = nums[i]
                if ans < dp:
                    ans_start = ans_end = i
                    ans = dp
            else:
                dp = nums[i] + dp
                if ans < dp:
                    ans_end = i
                    ans = dp
        return ans_start, ans_end, ans

    ans = [0, 0, 0, 0]
    ans_sum = float('-inf')
    m, n = len(matrix), len(matrix[0])
    presum = [[0 for _ in range(n)] for _ in range(m)]
    presum[0] = matrix[0].copy()
    for i in range(1, m):
        for j in range(n):
            presum[i][j] = presum[i-1][j] + matrix[i][j]

    for i in range(m):
        for j in range(i, m):
            nums = presum[j].copy()
            if i > 0:
                for k in range(n): nums[k] -= presum[i-1][k]

            start, end, max_sum = getStartEnd(nums)
            if max_sum > ans_sum:
                ans_sum = max_sum
                ans = [i, start, j, end]

    return ans

print(getMaxMatrix(
    [[-4, -5]]
))