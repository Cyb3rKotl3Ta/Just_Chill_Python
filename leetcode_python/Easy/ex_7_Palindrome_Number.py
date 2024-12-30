class Solution:
    def isPalindrome(self, x: int) -> bool:
        INT_MIN, INT_MAX = -2**31, 2**31 - 1
        if x < INT_MIN:
            return INT_MIN
        if x > INT_MAX:
            return INT_MAX

        x = str(x)
        if x == x[::-1]:return True
        else: return False

test = Solution()

test.isPalindrome(-121)
