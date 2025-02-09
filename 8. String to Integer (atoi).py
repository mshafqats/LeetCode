class Solution:
    def myAtoi(self, s: str) -> int:
        s = s.lstrip()

        if not s:
            return 0
        
        new_str = ""
        
        if s and (s[0] == "-" or s[0] == "+"):
            new_str += s[0]
            s = s[1:]
        
        for i in s:
            if i.isdigit():
                new_str += i
            else:
                break
        
        if new_str == "+" or new_str == "-":
            return 0
        
        result = int(new_str) if new_str else 0
        
        if result > 2147483647:
            return 2147483647
        if result < -2147483648:
            return -2147483648
        
        return result