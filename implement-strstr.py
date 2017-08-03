class Solution(object):
    def strStr(self, haystack, needle):
        """
        :type haystack: str
        :type needle: str
        :rtype: int
        """

        if not haystack and not needle:  # 边界检查,空字符串
            return 0

        for i in range(len(haystack)-len(needle)+1):  # 源字符串剩余长度必须大于目标字符串
            for j in range(len(needle)):
                if haystack[i+j] != needle[j]:
                    break
            else:  # not break
                return i
        return -1

solve = Solution()
print(solve.strStr('a', ''))