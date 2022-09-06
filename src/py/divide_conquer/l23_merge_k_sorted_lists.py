from typing import List, Optional

class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next

def mergeKLists(lists: List[Optional[ListNode]]) -> Optional[ListNode]:
    def mergeTwoLists(list1, list2):
        head = new_list = ListNode(-1)
        while list1 and list2:
            if list1.val < list2.val:
                head.next = list1
                list1 = list1.next
            else:
                head.next = list2
                list2 = list2.next
            head = head.next
        head.next = list1 if list1 else list2
        return new_list.next

    k = len(lists)
    prev_lists = lists
    new_lists = []
    while k > 1:
        for i in range(k >> 1):
            new_lists.append(mergeTwoLists(prev_lists[i * 2], prev_lists[i * 2 + 1]))
        if k & 1:
            new_lists.append(prev_lists[k - 1])
        new_lists, prev_lists = [], new_lists
        k = len(prev_lists)
    return prev_lists[0]

if __name__ == "__main__":
    vals = [[1, 4, 5], [1, 3, 4], [2, 6]]
    lists = []
    for l in vals:
        if not l:
            lists.append([])
            continue
        p = head = ListNode(val=l[0])
        for v in l[1:]:
            node = ListNode(val=v)
            p.next = node
            p = p.next
        lists.append(head)
    mergeKLists(lists=lists)


