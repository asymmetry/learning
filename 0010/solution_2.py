#!/usr/bin/env python3

# O(s*p)
# TODO: dynamic programming


class Solution:

    def isMatch(self, s, p):
        """
        :type s: str
        :type p: str
        :rtype: bool
        """

        pass


if __name__ == '__main__':
    print(Solution().isMatch('aa', 'a'))
    print(Solution().isMatch('aa', 'a*'))
    print(Solution().isMatch('ab', '.*'))
    print(Solution().isMatch('aab', 'c*a*b'))
    print(Solution().isMatch('mississippi', 'mis*is*p*.'))
