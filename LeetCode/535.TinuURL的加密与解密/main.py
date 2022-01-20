#!/usr/bin/env python

import random
import string

class Codec:
    alpha = string.digits + string.ascii_lowercase + string.ascii_uppercase
    _map = {}
    shortUrlRoot = "http://tinyurl.com/"

    def encode(self, longUrl: str) -> str:
        """Encodes a URL to a shortened URL.
        """
        key = "".join(random.sample(self.alpha, 6))
        while key in self._map:
            key = "".join(random.sample(self.alpha, 6))
        self._map[key] = longUrl
        return self.shortUrlRoot + key

    def decode(self, shortUrl: str) -> str:
        """Decodes a shortened URL to its original URL.
        """
        key = shortUrl.split("/")[-1]
        return self._map.get(key, "")


# Your Codec object will be instantiated and called as such:
# codec = Codec()
# codec.decode(codec.encode(url))