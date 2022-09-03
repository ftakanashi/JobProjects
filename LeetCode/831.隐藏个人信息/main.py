#!/usr/bin/env python

class Solution:
    def getEmail(self, email: str):
        username, domain = email.split("@")
        username = username.lower()
        domain = domain.lower()
        return f"{username[0]}*****{username[-1]}@{domain}"

    def getPhone(self, phone: str):
        digits = []
        for ch in reversed(phone):
            if not ch.isdigit(): continue
            digits.append(ch)
        digits.reverse()
        tail = "".join(digits[-4:])
        if len(digits) == 10:
            return f"***-***-{tail}"
        else:
            head = "+" + "*" * (len(digits) - 10)
            return f"{head}-***-***-{tail}"

    def maskPII(self, s: str) -> str:
        if "@" in s:
            return self.getEmail(s)
        else:
            return self.getPhone(s)