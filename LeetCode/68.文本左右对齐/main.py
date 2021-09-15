#!/usr/bin/env python
from typing import List

class Solution:
    def arrange(self, words: List[str], maxWidth: int, lastRow: bool) -> str:
        '''
        将一个词列表按题意组织成一个字符串
        :param words: 此列表
        :param maxWidth: 字符串最大长度限制
        :param lastRow: 标识是否是最后一行从而特殊处理
        '''
        num_gaps = len(words) - 1    # 空格的数量
        if num_gaps == 0:    # 只有一个单词时，直接补齐空格后返回
            return words[0] + ' ' * (maxWidth - len(words[0]))
        if lastRow:    # 当是最后一行时，直接用一个空格串联单词成字符串，补齐空格，返回
            s = ' '.join(words)
            return s + ' ' * (maxWidth - len(s))

        words_len = sum(len(word) for word in words)
        gaps_len = maxWidth - words_len    # 所有空格的总长度
        avg_len = gaps_len // num_gaps    # 平均空格的长度（由于空格要求尽量平均，若无法整除的情况，余出的部分从左到右加到空格中
        gaps = [avg_len for _ in range(num_gaps)]
        for i in range(gaps_len % num_gaps):
            gaps[i] += 1    # 处理余出的部分
        gaps.append(0)    # 为了下面输出方便，再加一个零长度的空格

        res = ''
        for i in range(len(words)):
            res += (words[i] + gaps[i] * ' ')
        return res

    def fullJustify(self, words: List[str], maxWidth: int) -> List[str]:
        lengths = [len(word) for word in words]
        n = len(words)
        i = 0
        res = []
        while i < n:    # 开始扫描
            row_len = 0    # 维护行的单词以及这些单词加上单词之间至少1个空格长度的总长度
            row = []
            # 开始收集可以放入一行的单词
            while i < n:
                row_len += lengths[i]
                row.append(words[i])
                if row_len >= maxWidth: break    # 如果加入某个单词后恰好长度达标，则无需加后续空格并可以直接break
                row_len += 1    # 否则加上额外的1个空格
                i += 1    # 继续扫描下个单词

            if row_len > maxWidth:    # 在这里若row_len > maxWidth，则说明当前row列表中最后一个单词加入后长度超标，需要将其去除
                i -= 1
                row.pop()
            # 将当前row中单词组织成字符串后加入res
            res.append(self.arrange(row, maxWidth, i==n))
            i += 1
        return res