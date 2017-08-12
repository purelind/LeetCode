class Solution(object):
    def lengthOfLongestSubstring(self, s):
        """
        :type s: str
        :rtype: int
        """
        usedChar = {}
        start = maxLength = 0
        for i, c in enumerate(s):
            if c in usedChar and start <= usedChar[c]:
                start = usedChar[c] + 1
            else:
                maxLength = max(maxLength, i-start+1)
            usedChar[c] = i
        return maxLength

solve = Solution()
print(solve.lengthOfLongestSubstring("abcabcbb"))