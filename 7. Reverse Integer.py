class Solution:
    def reverse(self, x: int) -> int:
        is_negative = x < 0
        x = abs(x)
        digits = list(str(x))
        reversed_digits = digits[::-1]
        reversed_str = ''.join(reversed_digits)
        reversed_int = int(reversed_str)
        if reversed_int > 2**31 - 1:
            return 0
        return reversed_int if not is_negative else -reversed_int