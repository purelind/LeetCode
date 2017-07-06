class Solution(object):
    def generate(self, numRows):
        """
        118. Pascal's Triangle
        Given numRows, generate the first numRows of Pascal's triangle.
        For example, given numRows = 5,
        Return
        [
            [1],
            [1,1],
            [1,2,1],
            [1,3,3,1],
            [1,4,6,4,1]
        ]
        :type numRows: int
        :rtype: List[List[int]]
        """
        pascal = []
        for currentRow in range(numRows):
            if currentRow == 0:
                pascal.append([1])
            elif currentRow == 1:
                pascal.append([1, 1])
            else:
                pascal.append([1])
                for nth in range(1, currentRow):
                    pascal[currentRow].append(pascal[currentRow-1][nth-1] + pascal[currentRow-1][nth])
                pascal[currentRow].append(1)
        return pascal

solve = Solution()
numRows = 1
print(solve.generate(numRows))


