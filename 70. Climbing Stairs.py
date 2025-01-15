'''
=====================
|  ID: MShafqatS    |
|  LANG: Python     |
=====================
Mohammad Shafqat Siddiqui
'''

class Solution:
    def climbStairs(self, n: int) -> int:
        s1, s2 = 1, 2
        if n == 1:
            return 1
        if n == 2:
            return 2
        for i in range(2, n):
            res = s1 + s2
            s1, s2 = s2, res
        return res
