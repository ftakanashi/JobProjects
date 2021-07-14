from typing import List

class Solution:
    def spiralOrder(self, matrix: List[List[int]]) -> List[int]:
        m, n = len(matrix), len(matrix[0])
        l = 0
        res = []
        while len(res) < m * n:

            j = l
            while j < n-l:
                res.append(matrix[l][j])
                j += 1
            res.pop()
            i = l
            while i < m-l:
                res.append(matrix[i][n-l-1])
                i += 1
            res.pop()
            j = n-l-1
            while j >= l:
                res.append(matrix[m-l-1][j])
                j -= 1
            res.pop()
            i = m-l-1
            while i >= l:
                res.append(matrix[i][l])
                i -= 1
            res.pop()

            l += 1

        return res

if __name__ == '__main__':
    s = Solution()
    res = s.spiralOrder([[1,2,3,],[4,5,6],[7,8,9]])
    print(res)