from typing import Optional


class SolutionNotCorrect:
    def removeNthFromEnd(self, head, n: int):
        length = len(head)
        index_to_remove = length - n

        if 0 <= index_to_remove < length:
            del head[index_to_remove]
        return head


# Definition for singly-linked list.
class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next


class Solution:
    def removeNthFromEnd(self, head: Optional[ListNode], n: int) -> Optional[ListNode]:
        # Створюємо фіктивний вузол перед головою для зручності
        dummy = ListNode(0, head)
        first = dummy
        second = dummy

        # Переміщуємо "first" вперед на n+1 кроків
        for _ in range(n + 1):
            first = first.next

        # Переміщуємо обидва вказівники до кінця списку
        while first:
            first = first.next
            second = second.next

        # Видаляємо n-ий вузол з кінця
        second.next = second.next.next

        # Повертаємо нову голову списку
        return dummy.next

sol = Solution()

print(sol.removeNthFromEnd(head = [1,2,3,4,5], n = 2))
