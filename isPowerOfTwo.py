class Solution(object):
    def isPowerOfTwo(self, n):
        """

        :param n: int
        :return: bool
        """
        count = 0
        # if n <= 0:
        #     return False
        hasOne = False
        while n > 0:
            if n & 1:
                if hasOne:
                    return False
                else:
                    hasOne = True
            n >>= 1
        return hasOne
solve = Solution()
print(solve.isPowerOfTwo(64))