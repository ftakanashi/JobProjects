#!/usr/bin/env python

from typing import List

class Solution:
    def displayTable(self, orders: List[List[str]]) -> List[List[str]]:
        menus = set()
        for _, _, m in orders:
            menus.add(m)
        m2i = {m: i for i, m in enumerate(sorted(menus))}
        info = {}
        for _, table, m in orders:
            table = int(table)
            if table not in info:
                info[table] = [0 for _ in range(len(menus))]
            info[table][m2i[m]] += 1

        title = ['Table',]
        title.extend(list(sorted(menus)))

        res = [title, ]
        for table in sorted(info):
            order_items = info[table]
            row = [str(table), ]
            row.extend([str(o) for o in order_items])
            res.append(row)
        return res