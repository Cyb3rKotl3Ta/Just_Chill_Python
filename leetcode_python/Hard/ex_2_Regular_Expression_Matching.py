class Solution:
    def isMatch(self, s: str, p: str) -> bool:
        print(p.strip('*'))
        if p == s and '*' not in p and '.' not in p: return True
        elif '.' in p and set(s) == p.strip('.'): return True
        elif '*' in p and set(s) in p.strip('*'): return True

test = Solution()
test.isMatch('aaabs', '*a')