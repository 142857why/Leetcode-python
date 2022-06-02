# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

from typing import List
from LinkedListHelper.linked_list import *


class Solution:
    def reorderList(self, head: ListNode) -> None:
        """
        Do not return anything, modify head in-place instead.
        """
        pass


if __name__ == '__main__':
    arr = [1, 2, 3, 4, 5]
    head = arrayToListNode(arr)
    prettyPrintLinkedList(head)

    sol = Solution()
    sol.reorderList(head)
    prettyPrintLinkedList(head)