from typing import Optional

from LinkedListHelper.linked_list import *


class Solution:
    def reverse(self, head: Optional[ListNode]) -> Optional[ListNode]:
        dummyHead = ListNode(0)
        while head is not None:
            p = head
            head = head.next
            p.next = dummyHead.next
            dummyHead.next = p
        return dummyHead.next

    def removeNodes(self, head: Optional[ListNode]) -> Optional[ListNode]:
        head = self.reverse(head)
        p = head
        while p.next is not None:
            if p.val > p.next.val:
                p.next = p.next.next
            else:
                p = p.next
        return self.reverse(head)


if __name__ == '__main__':
    solution = Solution()
    head = arrayToListNode([5, 2, 13, 15, 3, 8])
    prettyPrintLinkedList(solution.removeNodes(head))

