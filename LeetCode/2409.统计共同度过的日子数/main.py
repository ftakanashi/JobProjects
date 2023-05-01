#!/usr/bin/env python
# -*- coding:utf-8 -*-

# 月份和月份中最大天数的对应
month_days = [0, 31, 28, 31, 30, 31, 30, 31, 31, 30, 31, 30, 31]

class Date:
    """
    日期对象, datetime.datetime的平替
    只需要实现一个 __lt__ 或者 __gt__ 就能满足后续比大小的需求
    """
    def __init__(self, dateStr: str):
        self.month, self.day = map(int, dateStr.split("-"))

    def __lt__(self, other) -> bool:
        if self.month < other.month:
            return True
        elif self.month > other.month:
            return False
        else:
            return self.day < other.day


class Solution:
    def diff(self, day1: Date, day2: Date) -> int:
        """
        计算两个日期对象中间隔了多少天，datetime.timedelta 的平替
        """
        if day2 < day1:
            day1, day2 = day2, day1
        if day1.month == day2.month:
            return day2.day - day1.day + 1
        else:
            total = month_days[day1.month] - day1.day + 1
            for m in range(day1.month + 1, day2.month):
                total += month_days[m]
            total += day2.day
            return total

    def countDaysTogether(self, arriveAlice: str, leaveAlice: str, arriveBob: str, leaveBob: str) -> int:
        a_start, a_end, b_start, b_end = map(Date, [arriveAlice, leaveAlice, arriveBob, leaveBob])
        if a_start > b_start:
            a_start, b_start = b_start, a_start
            a_end, b_end = b_end, a_end

        if b_start > a_end:
            # 两个区间没有重叠
            return 0
        elif b_end > a_end:
            # 两个区间部分重叠
            return self.diff(a_end, b_start)
        else:
            # 两个区间完全重叠（b区间整个都被a区间包含了）
            return self.diff(b_start, b_end)