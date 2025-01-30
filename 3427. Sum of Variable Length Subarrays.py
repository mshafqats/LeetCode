class Solution:
    def subarraySum(self, nums: List[int]) -> int:
        result = 0
        for i in range(len(nums)):
            starting_index = max(0, i - nums[i])
            result += sum(nums[starting_index:i+1])
        return result