class Solution(object):
    def uniquePaths(self, m, n):
        """
        :type m: int
        :type n: int
        :rtype: int
        """
        if m > n:
            return self.uniquePaths(n,m)

        cur = [1 for i in range(m)]
        for j in range(1, n):
            for i in range(1, m):
                cur[i] += cur[i-1]
        return cur[m-1]

solve = Solution()
print(solve.uniquePaths(3, 3))
