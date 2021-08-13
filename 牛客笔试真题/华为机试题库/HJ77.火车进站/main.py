#!/usr/bin/env python
def process(trains):
    res = []
    n = len(trains)

    def dfs(pos, stack, subres):
        if pos == n:    # 终止dfs时别忘了将stack中剩余内容倒序加到subres中去形成完整结果。
            res.append(subres + list(reversed(stack)))
            return

        # 直接将当前元素入栈，此时不需要栈pop
        dfs(pos + 1, stack + [trains[pos]], subres)

        popped = []    # 构建popped数组，这是为了下面可以方便地构造新subres
        while stack:
            popped.append(stack.pop())
            dfs(pos + 1, stack + [trains[pos]], subres + popped)

    dfs(0, [], [])
    return res

def main():
    n = int(input())
    trains = [int(n) for n in input().strip().split()]
    res = process(trains)
    for row in sorted(res):
        print(' '.join(f'{i}' for i in row))


main()