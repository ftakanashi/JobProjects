#
# 代码中的类名、方法名、参数名已经指定，请勿修改，直接返回方法规定的值即可
#
# 获取最小运算此参数
# @param x int整型
# @param y int整型
# @return int整型
#
from collections import deque
class Solution:
    def getMinOpsCount(self , x , y ):
        # write code here
        if x > y: x, y = y, x
        base_ans = 0
        if y == 0: return abs(x)
        elif y > 0 and x <= 0:
            base_ans = abs(x) + 1
            x = 1
        elif y < 0:
            x, y = abs(y), abs(x)

        print(x, y, base_ans)

        queue = deque([(x, 0)])
        seen = set()
        while queue:
            num, cur = queue.popleft()
            if num in seen: continue
            seen.add(num)
            for cand in (num - 1, num + 1, num * 2):
                if cand == y: return cur + 1 + base_ans
                if cand not in seen:
                    queue.append((cand, cur + 1))

s = Solution()
res = s.getMinOpsCount(1, 200)
print(res)