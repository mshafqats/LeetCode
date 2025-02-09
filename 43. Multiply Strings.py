class Solution:
    def multiply(self, num1: str, num2: str) -> str:
        if int(num1) == 0 or int(num2) == 0:
            return "0"

        n1 = num1.lstrip('0')
        n2 = num2.lstrip('0')
        result = int(n1) * int(n2)
        return str(result)