class Solution(object):
    def findPeakElement(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        start = 0
        end = len(nums) - 1

        while start <= end:
            mid = (start + end) // 2
            if (mid == 0 or nums[mid] > nums[mid-1]) and (mid == len(nums)-1 or nums[mid] > nums[mid+1]):
                return mid
            elif mid > 0 and nums[mid-1] > nums[mid]:
                end = mid - 1
            else:
                start = mid +1

        return mid

solve = Solution()
print(solve.findPeakElement([3,2,1]))

