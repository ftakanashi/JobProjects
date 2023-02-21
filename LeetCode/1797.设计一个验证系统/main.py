#!/usr/bin/env python
# -*- coding:utf-8 -*-

class AuthenticationManager:

    def __init__(self, timeToLive: int):
        self.tokens = {}
        self.ttl = timeToLive

    def generate(self, tokenId: str, currentTime: int) -> None:
        self.tokens[tokenId] = currentTime + self.ttl

    def renew(self, tokenId: str, currentTime: int) -> None:
        if tokenId not in self.tokens or self.tokens[tokenId] <= currentTime:
            return

        self.tokens[tokenId] = currentTime + self.ttl

    def countUnexpiredTokens(self, currentTime: int) -> int:
        ans = 0
        for token in self.tokens:
            if self.tokens[token] > currentTime:
                ans += 1
        return ans

# Your AuthenticationManager object will be instantiated and called as such:
# obj = AuthenticationManager(timeToLive)
# obj.generate(tokenId,currentTime)
# obj.renew(tokenId,currentTime)
# param_3 = obj.countUnexpiredTokens(currentTime)