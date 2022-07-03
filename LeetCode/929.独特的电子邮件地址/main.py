#!/usr/bin/env python
from typing import List

import re
class Solution:
    def numUniqueEmails(self, emails: List[str]) -> int:
        send = set()
        for email in emails:
            m = re.match("^(.+?)@(.+)$", email)
            local = m.group(1).split("+")[0].replace(".", "")
            domain = m.group(2)
            send.add(f"{local}@{domain}")
        # print(send)
        return len(send)