class Solution(object):
    def isPalindrome(self, x):
        """
        Determine whether an integer is a palindrome. Do this without extra space.
        :type x: int
        :rtype: bool
        """
        if x < 0:
            return False
        else:
            xCopy = x
            reverseNum = 0
            while xCopy:
                reverseNum = reverseNum * 10 + xCopy % 10
                xCopy = xCopy // 10
            if reverseNum == x:
                return True
            else:
                return False

solve = Solution()
print(solve.isPalindrome(1221))