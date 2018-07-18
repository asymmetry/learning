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

    def mergeTwoLists(self, l1, l2):
        """
        :type l1: ListNode
        :type l2: ListNode
        :rtype: ListNode
        """

        root = ListNode(None)

        pointer = root
        while l1 is not None and l2 is not None:
            if l1.val <= l2.val:
                pointer.next = l1
                pointer = pointer.next
                l1 = l1.next
            else:
                pointer.next = l2
                pointer = pointer.next
                l2 = l2.next

        if l1 is not None:
            pointer.next = l1

        if l2 is not None:
            pointer.next = l2

        return root.next


if __name__ == '__main__':
    list1 = [1, 2, 4]
    l1 = ListNode(list1[0])
    pointer = l1
    for val in list1[1:]:
        pointer.next = ListNode(val)
        pointer = pointer.next

    list2 = [1, 3, 4]
    l2 = ListNode(list2[0])
    pointer = l2
    for val in list2[1:]:
        pointer.next = ListNode(val)
        pointer = pointer.next

    result = Solution().mergeTwoLists(l1, l2)

    print_list(result)
