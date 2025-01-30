class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        if not s:
            return 0
        if len(s) == 1:
            return 1
        longest_substring_len = 0
        start = 0
        present_chars = {}
        for i in range(len(s)):
            char = s[i]
            if char in present_chars:
                start = max(start, present_chars[char] + 1)
            present_chars[char] = i
            longest_substring_len = max(longest_substring_len, i - start + 1)
        return longest_substring_len