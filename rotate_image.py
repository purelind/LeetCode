class Solution(object):
    def rotate(self, matrix):
        """
        :type matrix: List[List[int]]
        :rtype: void Do not return anything, modify matrix in-place instead.
        """
        matrix_copy = list(reversed(matrix))
        for i in range(len(matrix)):
            matrix[i] = matrix_copy[i]

        for i in range(len(matrix)):
            for j in range(i+1,len(matrix[i])):
                matrix[i][j], matrix[j][i] = matrix[j][i], matrix[i][j]


matrixlist = [[1, 2, 3],
              [4, 5, 6],
              [7, 8, 9]]
solve = Solution()
solve.rotate(matrixlist)
print(matrixlist)
