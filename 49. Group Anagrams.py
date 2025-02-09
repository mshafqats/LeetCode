class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        anagram_dict = {}
        for i in strs:
            sorted_strs = ''.join(sorted(i))
            if sorted_strs in anagram_dict:
                anagram_dict[sorted_strs].append(i)
            else:
                anagram_dict[sorted_strs] = [i]
            
        return sorted(anagram_dict.values())