class Solution(object):
    def findMin(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        if not nums:
            return
        lo = 0
        hi = len(nums)-1
        mid = (lo + hi) // 2
        while lo < hi:
            if nums[lo] < nums[hi]:
                return nums[lo]
            else:
                if nums[lo] == nums[mid]:
                    lo += 1
                    mid = (lo + hi) // 2
                elif nums[lo] < nums[mid]:
                    lo = mid
                    mid = (lo + hi) // 2
                elif nums[lo] > nums[mid]:
                    hi = mid
                    mid = (lo + hi) // 2
        return nums[lo]

solve = Solution()
print(solve.findMin([4,4,4,5,6,7,7,0,0,1,1,4,4]))