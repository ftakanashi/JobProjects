#!/usr/bin/env python
from typing import List

class Solution:
    def outerTrees(self, points: List[List[int]]) -> List[List[int]]:

        def cross(p, q, r):
            '''
            向量pq与向量qr的外积求算函数
            参考官方答案： https://leetcode-cn.com/problems/erect-the-fence/
            '''
            return (q[0] - p[0]) * (r[1] - q[1]) - (q[1] - p[1]) * (r[0] - q[0])

        n = len(points)
        if n < 4: return points    # 若小于等于三点，根据题意，所有点都在答案中

        start = min(enumerate(points), key=lambda x: x[1][0])[0]    # 寻找最靠左的点
        ans = [points[start], ]
        used = set([start, ])
        p = start  # 初始状态下，保证p是整个凸包最靠左的点（之一）
        # 开始循环，整个探索过程是从整个图的最靠左的点开始，沿着逆时针方向进行凸包的连接
        while True:

            # 从任意一个非P点开始，寻找对于P点而言最接近能完成逆时针合围的点，令其为点Q
            q = (p + 1) % n
            for r in range(n):    # 注意，这里并不能因为r已经在used中就不去遍历，因为即使如此也可能需要r作为跳板去寻找凸包下一条边
                if cross(points[p], points[q], points[r]) < 0:
                    q = r
            # 在这个时间点上，PQ是一条逆时针视图连接起凸包的边

            # 为了保证不漏掉任何一点，进一步搜索PQ方向上也在同一直线上的点，加入答案
            for i in range(n):
                if i not in used and i not in (p, q) and cross(points[p], points[q], points[i]) == 0:
                    ans.append(points[i])
                    used.add(i)

            if q == start:    # 凸包连接完成，跳出循环
                break
            else:
                if q not in used:    # 为了避免重复的点进入答案，因为此时的q有可能是前几轮迭代中由于和某边在同一直线上而被加入过答案了
                    ans.append(points[q])
                    used.add(q)
                p = q

        return ans