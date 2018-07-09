#!/usr/bin/env python3


# Definition for singly-linked list.
class ListNode:

    def __init__(self, x):
        self.val = x
        self.next = None


class Solution:

    def addTwoNumbers(self, l1, l2):
        """
        :type l1: ListNode
        :type l2: ListNode
        :rtype: ListNode
        """

        return self._recursionAddTwoNumbers(l1, l2, 0)

    def _recursionAddTwoNumbers(self, l1, l2, carry):
        if l1 is None and l2 is None:
            if carry > 0:
                return ListNode(carry)
            else:
                return None

        if l1 is None:
            sum_ = l2.val + carry
            r = ListNode(sum_ % 10)
            r.next = self._recursionAddTwoNumbers(None, l2.next, sum_ // 10)
        elif l2 is None:
            sum_ = l1.val + carry
            r = ListNode(sum_ % 10)
            r.next = self._recursionAddTwoNumbers(l1.next, None, sum_ // 10)
        else:
            sum_ = l1.val + l2.val + carry
            r = ListNode(sum_ % 10)
            r.next = self._recursionAddTwoNumbers(l1.next, l2.next, sum_ // 10)

        return r


if __name__ == '__main__':
    l1 = ListNode(2)
    l1.next = ListNode(4)
    l1.next.next = ListNode(3)
    l2 = ListNode(5)
    l2.next = ListNode(6)
    l2.next.next = ListNode(4)

    result = Solution().addTwoNumbers(l1, l2)

    print(result.val, end='')
    while result.next is not None:
        result = result.next
        print(f' -> {result.val}', end='')
    print('')
