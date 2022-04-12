#!/usr/bin/env python
class Solution:
    def reachingPoints(self, sx: int, sy: int, tx: int, ty: int) -> bool:
        while tx != ty:
            if tx == ty: return False
            if tx > ty:
                tx -= max(1, (tx - sx) // ty) * ty
            else:
                ty -= max(1, (ty - sy) // tx) * tx

            if tx == sx and ty == sy: return True

        return tx == sx and ty == sy