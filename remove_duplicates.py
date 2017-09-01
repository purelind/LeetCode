class Solution(object):
    def removeDuplicates(self, nums):
        """
        Given a sorted array, remove the duplicates in place such that each element appear only once and return the new
        length.
        Do not allocate extra space for another array, you must do this in place with constant memory.
        For example,
        Given input array nums = [1,1,2],
        Your function should return length = 2, with the first two elements of nums being 1 and 2 respectively. It
        doesn't matter what you leave beyond the new length.
        corner case: []
        :type nums: List[int]
        :rtype: int
        """
        if not nums:
            return 0
        currentIndex = 0
        for searchIndex in range(1, len(nums)):
            if nums[searchIndex] == nums[currentIndex]:
                continue
            currentIndex += 1
            nums[currentIndex] = nums[searchIndex]
        return currentIndex + 1

solve = Solution()
nums = [1]
print(solve.removeDuplicates(nums))
print(nums)
