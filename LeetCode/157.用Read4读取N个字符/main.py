#!/usr/bin/env python

"""
The read4 API is already defined for you.

    @param buf4, a list of characters
    @return an integer
    def read4(buf4):

# Below is an example of how the read4 API can be called.
file = File("abcdefghijk") # File is "abcdefghijk", initially file pointer (fp) points to 'a'
buf4 = [' '] * 4 # Create buffer with enough space to store characters
read4(buf4) # read4 returns 4. Now buf = ['a','b','c','d'], fp points to 'e'
read4(buf4) # read4 returns 4. Now buf = ['e','f','g','h'], fp points to 'i'
read4(buf4) # read4 returns 3. Now buf = ['i','j','k',...], fp points to end of file
"""

def read4(buf):
    return 4

class Solution:
    def read(self, buf, n):
        """
        :type buf: Destination buffer (List[str])
        :type n: Number of characters to read (int)
        :rtype: The number of actual characters read (int)
        """
        read_cnt, read_len = 0, 1
        while read_cnt < n and read_len > 0:
            tmp = [None] * 4
            read_len = read4(tmp)

            i = 0
            while i < read_len and read_cnt < n:
                buf[read_cnt] = tmp[i]
                read_cnt += 1
                i += 1

        return read_cnt