class Solution(object):
    def missingNumber(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        valueXor = 0
        for item in range(len(nums)+1):
            valueXor ^= item
        for item in nums:
            valueXor ^= item
        return valueXor

solve = Solution()
print(solve.missingNumber([1,2,3]))
