'''
=====================
|  ID: MShafqatS    |
|  LANG: Python     |
=====================
Mohammad Shafqat Siddiqui
'''

class Solution:
    def addBinary(self, a: str, b: str) -> str:
        value_a = int(a, 2)
        value_b = int(b, 2)
        result = value_a + value_b
        return bin(result)[2:]
