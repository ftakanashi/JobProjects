#!/usr/bin/env python

class Solution:
    def intToRoman(self, num: int) -> str:
        char_map = ['IVX', 'XLC', 'CDM', 'MPP']
        n2s = [
            '', '{a}', '{a}'*2, '{a}'*3, '{a}{b}', '{b}',
            '{b}{a}', '{b}'+'{a}'*2, '{b}'+'{a}'*3, '{a}{c}'
        ]

        res = ''
        base = 0
        while num > 0:
            digit = num % 10
            a, b, c = char_map[base]
            res = n2s[digit].format(a=a, b=b, c=c) + res
            num = num // 10
            base += 1

        return res