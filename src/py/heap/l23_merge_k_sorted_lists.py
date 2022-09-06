from typing import List, Optional
from queue import PriorityQueue
from heapq import heappush, heappop

class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next

def mergeKLists(lists: List[Optional[ListNode]]) -> Optional[ListNode]:
    """
    LC 23: You are given an array of k linked-lists lists, each linked-list is sorted in ascending order.
    Merge all the linked-lists into one sorted linked-list and return it.

    Note: Compare every k nodes (head of every linked list) and get the node with the smallest value, time is O(KN),
    since almost every selection of node in final linked costs O(k) (k-1 times comparison).

    -->   Optimize the comparison process by priority queue,
          Time: O(Nlog(K)). each comparison (insertion/deletion): O(logK); get the min: O(1)
          Space: O(N) create new lined list; O(k) create priority queue
    """
    res = None  # res: new sorted linklist
    cur = None  # pointer the last element in new sorted linklist
    h = []      # heap: (val, lists index)
    for i, l in enumerate(lists):
        if not l:
            continue
        ###################################
        # don't make heappush(h, (l.val, l)) because heap may compare second element `l` in a tuple
        # if l.val is not unique. so we put `l.val` and index `i` in the tuple.
        heappush(h, (l.val, i))
        lists[i] = lists[i].next
    while h:
        v, i = heappop(h)
        if not res:
            cur = res = ListNode(v)
        else:
            cur.next = ListNode(v)
            cur = cur.next
        if lists[i]:
            heappush(h, (lists[i].val, i))
            lists[i] = lists[i].next
    return res




if __name__ == "__main__":
    mergeKLists([ListNode(5), ListNode(3), ListNode(9), ListNode(2),  ListNode(4), ListNode(8)])
