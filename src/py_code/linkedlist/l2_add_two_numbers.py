from src.py_code.linkedlist import ListNode
from typing import Optional

def addTwoNumbers(l1:Optional[ListNode], l2:Optional[ListNode]) -> Optional[ListNode]:
    dummy_head = ListNode(0)
    curr = dummy_head
    carry = 0
    while l1 != None or l2 != None or carry !=0:
        l1_val = l1.val if l1 else 0
        l2_val = l2.val if l2 else 0
        column_sum = l1_val + l2_val + carry
        carry = column_sum // 10
        curr.next = ListNode(column_sum % 10)
        curr = curr.next
        l1 = l1.next if l1 else None
        l2 = l2.next if l2 else None
    return dummy_head.next