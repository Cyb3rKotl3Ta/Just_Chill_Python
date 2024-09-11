class Solution:
    def reverse(self, x: int) -> int:
        sign = -1 if x < 0 else 1

        reversed_str = str(abs(x))[::-1]
        reversed_int = int(reversed_str) * sign

        if reversed_int not in range(-2**31, (2**31)-1):
            return 0

        return reversed_int

res = Solution()
print(res.reverse(-321))