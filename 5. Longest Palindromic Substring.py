class Solution:
    def expand_around_center(self, s, left, right):
        while left>=0 and right<len(s) and s[left]==s[right]:
            left -= 1
            right += 1
        return s[left + 1:right]

    def longestPalindrome(self, s: str) -> str:
        largest_substring = ""
        for i in range(len(s)):
            p1 = self.expand_around_center(s, i, i)
            p2 = self.expand_around_center(s, i, i+1)
            largest_substring = max(largest_substring, p1, p2, key=len)
        return largest_substring