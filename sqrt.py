class Solution(object):
    def mySqrt(self, x):
        """
        :type x: int
        :rtype: int
        """
        def improve(guess, x):
            return (guess + (x/guess)) / 2

        def good_Enough(guess, x):
            return abs(guess*guess - x) < 0.001

        def sqrt_iter(guess, x):
            if good_Enough(guess, x):
                return guess
            else:
                return sqrt_iter(improve(guess, x), x)

        return int(sqrt_iter(1.0, x))

solve = Solution()
print(solve.mySqrt(4))