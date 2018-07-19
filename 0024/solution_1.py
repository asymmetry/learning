#!/usr/bin/env python3


def print_list(l):
    if l is None:
        print('')
        return

    print(l.val, end='')
    while l.next is not None:
        l = l.next
        print(f' -> {l.val}', end='')
    print('')


# Definition for singly-linked list.
class ListNode:

    def __init__(self, x):
        self.val = x
        self.next = None


class Solution:

    def swapPairs(self, head):
        """
        :type head: ListNode
        :rtype: ListNode
        """

        if head is None:
            return head

        first, second = head, head

        if second.next is not None:
            second = second.next
            head = second
            first.next, second.next = second.next, first
            first, second = second, first

        while second.next is not None and second.next.next is not None:
            save = second
            first = first.next.next
            second = second.next.next
            save.next = second
            first.next, second.next = second.next, first
            first, second = second, first

        return head


if __name__ == '__main__':
    list1 = [1, 2, 3, 4]
    l1 = ListNode(list1[0])
    pointer = l1
    for val in list1[1:]:
        pointer.next = ListNode(val)
        pointer = pointer.next

    result = Solution().swapPairs(l1)

    print_list(result)
