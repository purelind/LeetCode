class Solution(object):
    def getRow(self, rowIndex):
        """
        :type rowIndex: int
        :rtype: List[int]
        """
        pascal = []
        for row in range(rowIndex+1):
            if row == 0:
                pascal.append(1)
            elif row == 1:
                pascal.append(1)
            else:
                for nth in range(row-1, 0, -1):
                    pascal[nth] = pascal[nth-1] + pascal[nth]
                pascal.append(1)
        return pascal

solve = Solution()
rowIndex = 4
print(solve.getRow(rowIndex))

