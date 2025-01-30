class Solution:
    def findEvenNumbers(self, n: List[int]) -> List[int]:
        nums = []
        c = Counter(n)
        for i in range(1, 10):
            for j in range(0, 10):
                for k in range(0, 9, 2):
                    c1 = Counter([i, j, k])
                    if c1 <= c:
                        nums.append(i * 100 + j * 10 + k) 
        return sorted(nums)