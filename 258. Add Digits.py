class Solution:
    def addDigits(self, num: int) -> int:
        if num < 10:
            return num
        nums_str = str(num)
        result = sum(int(i) for i in nums_str)
        return self.addDigits(result)