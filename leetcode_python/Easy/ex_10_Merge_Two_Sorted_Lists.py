class Solution:
    def mergeTwoLists(self, list1: list, list2: list) -> list:
        return sorted(list1 + list2)


list1 = [1,2,4]
list2 = [1,3,4]
sol = Solution()
print(sol.mergeTwoLists(list1, list2))