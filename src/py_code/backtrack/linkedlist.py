#!/bin/python3

import math
import os
import random
import re
import sys

class SinglyLinkedListNode:
    def __init__(self, node_data):
        self.data = node_data
        self.next = None

class SinglyLinkedList:
    def __init__(self):
        self.head = None
        self.tail = None

    def insert_node(self, node_data):
        node = SinglyLinkedListNode(node_data)

        if not self.head:
            self.head = node
        else:
            self.tail.next = node

        self.tail = node



#
# Complete the 'reversingLinkedList' function below.
#
# The function is expected to return an INTEGER_SINGLY_LINKED_LIST.
# The function accepts INTEGER_SINGLY_LINKED_LIST head as parameter.
#

#
# For your reference:
#
# SinglyLinkedListNode:
#     int data
#     SinglyLinkedListNode next
#
#

def reversingLinkedList(head):
    p = head
    n = 0
    numbers = [0]
    while p:
        numbers.append(p.data)
        n = n + 1
        p = p.next
    p = head

    i = 1
    while p:
        # fptr.write(str(p.data))
        # fptr.write('\n')
        if i & 1:
            p.data = numbers[n+1-i]
        p = p.next
        i = i + 1
    return head


if __name__ == '__main__':

    head_count = int(input().strip())

    head = SinglyLinkedList()

    for _ in range(head_count):
        head_item = int(input().strip())
        head.insert_node(head_item)

    result = reversingLinkedList(head.head)
