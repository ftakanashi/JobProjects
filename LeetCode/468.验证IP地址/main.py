#!/usr/bin/env python
class Solution:
    def checkIPv4(self, ip: str) -> bool:
        num_strs = ip.split(".")
        if len(num_strs) != 4: return False
        for num_str in num_strs:
            try:
                num = int(num_str)
            except Exception as e:
                return False
            if num_str[0] == "0":
                if (num == 0 and num_str != "0") or num != 0: return False
            if not (0 <= num <= 255): return False
        return True

    def checkIPv6(self, ip: str) -> bool:
        num_strs = ip.split(":")
        if len(num_strs) != 8: return False
        for num_str in num_strs:
            if len(num_str) > 4: return False
            try:
                num = int(num_str, 16)
            except Exception as e:
                return False
        return True

    def validIPAddress(self, queryIP: str) -> str:
        if self.checkIPv4(queryIP):
            return "IPv4"
        elif self.checkIPv6(queryIP):
            return "IPv6"
        else:
            return "Neither"