class Solution(object):
    def removeElement(self, nums, val):
        """
        Given an array and a value, remove all instances of that value in place and return the new length.
        Do not allocate extra space for another array, you must do this in place with constant memory.
        The order of elements can be changed. It doesn't matter what you leave beyond the new length.
        :type nums: List[int]
        :type val: int
        :rtype: int
        """
        recordIndex = 0
        for i in range(len(nums)):
            if nums[i] == val:
                continue
            nums[recordIndex] = nums[i]
            recordIndex += 1
        return recordIndex

solve = Solution()
nums = [3, 2, 2, 3]
print(solve.removeElement(nums, 3))
print(nums)
