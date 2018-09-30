class Solution:
    def lengthOfLastWord(self, s):
        """
        :type s: str
        :rtype: int
        """
        i = 1
        count = 0
        while i <= len(s):
            if count and s[-i] == ' ':
                return count
            elif s[-i] != ' ':
                count += 1
            else:
                pass
            i += 1
        return count


if __name__ == '__main__':
    print(Solution().lengthOfLastWord('a'))
