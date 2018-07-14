#!/usr/bin/env python3


# Definition for singly-linked list.
class ListNode:

    def __init__(self, x):
        self.val = x
        self.next = None


class Solution:

    def removeNthFromEnd(self, head, n):
        """
        :type head: ListNode
        :type n: int
        :rtype: ListNode
        """

        dummy = ListNode(None)
        dummy.next = head
        pointer, remove = dummy, dummy

        for _ in range(n):
            pointer = pointer.next

        while pointer.next is not None:
            remove = remove.next
            pointer = pointer.next

        remove.next = remove.next.next

        return dummy.next


if __name__ == '__main__':
    root = ListNode(1)
    pointer = root

    for i in range(2, 6):
        pointer.next = ListNode(i)
        pointer = pointer.next

    result = Solution().removeNthFromEnd(root, 5)

    print(result.val, end='')
    while result.next is not None:
        result = result.next
        print(f' -> {result.val}', end='')
    print('')
