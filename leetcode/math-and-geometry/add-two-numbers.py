from typing import Optional

class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next


class Solution:
    def addTwoNumbers(self, l1: Optional[ListNode], l2: Optional[ListNode]) -> Optional[ListNode]:
        dummy = ListNode(0)
        atual = dummy
        carry = 0

        while l1 or l2 or carry:
            v1 = l1.val if l1 else 0
            v2 = l2.val if l2 else 0

            soma = v1 + v2 + carry

            carry = soma // 10
            val = soma % 10

            atual.next = ListNode(val)

            atual = atual.next
            if l1: l1 = l1.next
            if l2: l2 = l2.next

        # Retorna o próximo do dummy, que é onde a soma real começou
        return dummy.next