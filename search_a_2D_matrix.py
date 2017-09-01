class Solution(object):
    def searchMatrix(self, matrix, target):
        """
        :type matrix: List[List[int]]
        :type target: int
        :rtype: bool
        """
        if not matrix:
            return False
        row = 0
        col = len(matrix[0])-1
        while row < len(matrix) and col >= 0:
            if target < matrix[row][col]:
                col -= 1
            elif target > matrix[row][col]:
                row += 1
            else:
                return True
        return False

solve = Solution()
print(solve.searchMatrix([[]], 0))
