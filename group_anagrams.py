class Solution(object):
    def groupAnagrams(self, strs):
        """
        :type strs: List[str]
        :rtype: List[List[str]]
        """
        strDict = {}
        result = []
        for i in range(len(strs)):
            string = strs[i]
            if "".join(sorted(string)) not in strDict:
                strDict["".join(sorted(string))] = [string]
            else:
                strDict["".join(sorted(string))].append(string)
        for each_key in strDict:
            result.append(strDict[each_key])
        return result

solve = Solution()
print(solve.groupAnagrams(["eat", "tea", "tan", "ate", "nat", "bat"]))

