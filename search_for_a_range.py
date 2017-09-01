class Solution(object):
    def searchRange(self, nums, target):
        """
        Given an array of integers sorted in ascending order, find the starting and ending position of a given target value.
        Your algorithm's runtime complexity must be in the order of O(log n).
        If the target is not found in the array, return [-1, -1].
        For example,
        Given [5, 7, 7, 8, 8, 10] and target value 8,
        return [3, 4].
        :type nums: List[int]
        :type target: int
        :rtype: List[int]
        """
        lo = 0
        length = len(nums)
        hi = length - 1
        mid = (lo + hi) // 2
        startIndex = -1
        endingIndex = -1

        # find the first target element
        while lo <= hi:
            if target > nums[mid]:
                lo = mid+1
                mid = (lo + hi) // 2
            else:
                hi = mid-1 # if mid element equals to target, decrease hi to mid-1
                mid = (lo + hi) // 2

        # if target element found, record index, else return[-1, -1]
        if lo < length and target == nums[lo]:
            startIndex = lo
        else:
            return [startIndex, endingIndex]

        lo2 = startIndex
        hi2 = length - 1
        mid2 = (lo2 + hi2) // 2

        # find the last target element
        while lo2 <= hi2:
            if target >= nums[mid2]: # if mid element equals to target, increase lo to mid2+1
                lo2 = mid2+1
                mid2 = (lo2 + hi2) // 2
            else:
                hi2 = mid2-1
                mid2 = (lo2 + hi2) // 2
        endingIndex = hi2

        return [startIndex, endingIndex]

solve = Solution()
print(solve.searchRange([5,7,7,8,8,9,10], 8))



