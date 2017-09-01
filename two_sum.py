class Solution(object):
    def twoSum(self, nums, target):
        """
        :type nums: List[int]
        :type target: int
        :rtype: List[int]
        """
        for i in range(len(nums)):
            numsCopy = nums[:]
            numsCopy.pop(i)
            if target-nums[i] in numsCopy:
                break
        for j in range(len(nums)):
            if nums[j] == target-nums[i] and i != j:
                break
        return [i, j]

No_1 = Solution()
No_1.twoSum([2, 7, 11, 15], 9)
print(No_1)
