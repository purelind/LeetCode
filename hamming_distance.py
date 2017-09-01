class Solution(object):
    def hammingDistance(self, x, y):
        """
        :type x: int
        :type y: int
        :rtype : int
        """
        def numberOfOneBits(intNumber):
            """
            :type inNumber: int
            :rtype        : int
            """
            count = 0
            for i in range(32):
                count += intNumber & 1
                intNumber >>= 1
            return count
        return numberOfOneBits(x ^ y)

solve = Solution()
print(solve.hammingDistance(4, 1))
