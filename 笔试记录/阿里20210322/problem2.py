#!/usr/bin/env python

import sys
def process(all_nums):

    mem = {}
    s, prefix_sum = 0, []
    for n in all_nums:
        s += n
        prefix_sum.append(s)

    def dfs(i, j, score):
        if i == j: return score
        if (i, j) in mem: return mem[(i, j)]
        max_score = score
        for start in range(i + 1, j + 1):
            pref_sum = prefix_sum[start - 1] - (prefix_sum[i - 1] if i > 0 else 0)
            rear_sum = prefix_sum[j] - pref_sum
            if pref_sum < rear_sum:
                s = dfs(i, start - 1, score + pref_sum)
            elif pref_sum > rear_sum:
                s = dfs(start, j, score + rear_sum)
            else:
                s = max(dfs(i, start - 1, score + pref_sum), dfs(start, j, score + rear_sum))
            max_score = max(s, max_score)

        mem[(i, j)] = max_score
        return max_score

    return dfs(0, len(all_nums) - 1, 0)


def main():
    # lines = sys.stdin.read().strip().split('\n')
    # nums = [int(i) for i in lines[1].strip().split()]
    nums = [6,2,3,4,5,5]
    ans = process(nums)
    print(ans)

if __name__ == '__main__':
    main()