'''
=====================
|  ID: MShafqatS    |
|  LANG: Python     |
=====================
Mohammad Shafqat Siddiqui
'''

class Solution:
    def mySqrt(self, x: int) -> int:
        i = 1
        while i <= x/i:
            i += 1
        return i-1
