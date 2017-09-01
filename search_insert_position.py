class Solution(object):
    def searchInsert(self, nums, target):
        """
        :type nums: List[int]
        :type target: int
        :rtype: int
        """
        lo = 0
        hi = len(nums) - 1

        while lo <= hi:
            mid = (lo + hi) // 2
            if target == nums[mid]:
                return mid
            elif target < nums[mid]:
                hi = mid - 1
            else:
                lo = mid + 1
        return lo

solve = Solution()
print(solve.searchInsert([], 0))
