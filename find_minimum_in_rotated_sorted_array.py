class Solution(object):
    def findMin(self, nums):
        """
        Suppose an array sorted in ascending order is rotated at some pivot unknown to you beforehand.
        (i.e., 0 1 2 4 5 6 7 might become 4 5 6 7 0 1 2).
        Find the minimum element.
        You may assume no duplicate exists in the array.
        :type nums: List[int]
        :rtype: int
        """
        lo = 0
        hi = len(nums)-1
        if not nums:
            return
        if not nums[lo] > nums[hi]:
            return nums[lo]
        mid = (lo + hi) // 2
        while lo < hi:
            if nums[mid] == nums[lo]:
                return nums[lo+1]
            if nums[mid] > nums[lo]:
                lo = mid
                mid = (lo + hi) // 2
            else:
                hi = mid
                mid = (lo + hi) // 2

solve = Solution()
print(solve.findMin([]))