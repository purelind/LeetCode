class Solution(object):
    def longestConsecutive(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        res = 0
        hashmap = dict()
        for n in nums:
            if not hashmap.get(n):
                left = hashmap.get(n-1, 0)
                right = hashmap.get(n+1, 0)
                all_sum = left + right + 1
                hashmap[n] = all_sum

                res = max(res, all_sum)

                hashmap[n-left] = all_sum
                hashmap[n+right] = all_sum

        return res



