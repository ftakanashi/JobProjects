#!/usr/bin/env python
class Codec1:
    def encode(self, strs: [str]) -> str:
        """Encodes a list of strings to a single string.
        """
        return " ||| ".join(strs)

    def decode(self, s: str) -> [str]:
        """Decodes a single string to a list of strings.
        """
        return s.split(" ||| ")

class Codec2:
    def encodeWithLen(self, s: str) -> str:
        l = len(s)
        str_l = hex(l)[2:]
        while len(str_l) < 4:
            str_l = "0" + str_l
        return str_l + s

    def encode(self, strs: [str]) -> str:
        """Encodes a list of strings to a single string.
        """
        return "".join([self.encodeWithLen(s) for s in strs])

    def decode(self, s: str) -> [str]:
        """Decodes a single string to a list of strings.
        """
        i = 0
        n = len(s)
        res = []
        while i < n:
            str_l = int(s[i:i+4], 16)
            i += 4
            res.append(s[i:i+str_l])
            i += str_l
        return res

# Your Codec object will be instantiated and called as such:
# codec = Codec()
# codec.decode(codec.encode(strs))