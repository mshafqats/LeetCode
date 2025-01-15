'''
=====================
|  ID: MShafqatS    |
|  LANG: Python     |
=====================
Mohammad Shafqat Siddiqui
'''

class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        n1 = len(nums)
        for i in range(n1-1):
            for j in range(i+1, n1):
                if nums[i] + nums[j] == target:
                    return [i, j]
        return []
