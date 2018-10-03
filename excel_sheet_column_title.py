class Solution(object):
    def convertToTitle(self, n):
        """
        :type n: int
        :rtype: str
        """
        import string
        ABC = string.ascii_uppercase
        if n <= 26:
            return ABC[n - 1]
        else:
            return self.convertToTitle((n-1) // 26) + self.convertToTitle(n % 26)


if __name__ == '__main__':
    print(Solution().convertToTitle(53))