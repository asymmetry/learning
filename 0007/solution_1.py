#!/usr/bin/env python3

# O(log(x))


class Solution:

    def reverse(self, x):
        """
        :type x: int
        :rtype: int
        """

        sign = 1 if x >= 0 else -1

        x = abs(x)

        result = 0
        while x > 0:
            result = result * 10 + x % 10
            x = x // 10

        result = sign * result

        if result > 2147483647 or result < -2147483648:
            result = 0

        return result


if __name__ == '__main__':
    print(Solution().reverse(123))
    print(Solution().reverse(-123))
    print(Solution().reverse(120))
