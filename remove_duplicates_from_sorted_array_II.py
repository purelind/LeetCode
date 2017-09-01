class Solution(object):
    def removeDuplicates(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        if not nums:
            return 0
        count = 0
        currentIndex = 0
        for searchIndex in range(1, len(nums)):
            if nums[searchIndex] == nums[currentIndex]:
                count += 1
                if count == 1:
                    currentIndex += 1
                    nums[currentIndex] = nums[searchIndex]
                continue
            count = 0
            currentIndex += 1
            nums[currentIndex] = nums[searchIndex]
        return currentIndex + 1

solve = Solution()
nums = []
print(solve.removeDuplicates(nums))
print(nums)
