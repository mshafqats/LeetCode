'''
=====================
|  ID: MShafqatS    |
|  LANG: Python     |
=====================
Mohammad Shafqat Siddiqui
'''

class Solution:
    def lengthOfLastWord(self, s: str) -> int:
        without_spaces = s.strip().split()
        count = 0
        for i in without_spaces[-1]:
            count += 1
        return count
