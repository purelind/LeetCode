class Solution(object):
    def reverse(self, x):
        """
        :type x: int
        :rtype: int
        """
        if x > 0:
            s = 1
        elif x < 0:
            s = -1
        else:
            s = 0
        r = int(str(abs(x))[::-1])
        return r*s*(r < 2**31)

solve = Solution()
print(solve.reverse(-23))