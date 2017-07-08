class Solution(object):
    def largestRectangleArea(self, heights):
        """
        Given n non-negative integers representing the histogram's bar height where the width of each bar is 1, find
        the area of largest rectangle in the histogram.
        :type heights: List[int]
        :rtype: int
        """
        stack = []
        heights.append(0)
        maxRectangleArea = 0
        searchIndex = 0
        length = len(heights)
        while searchIndex < length:
            if not stack or heights[searchIndex] > heights[stack[-1]]:
                stack.append(searchIndex)
                searchIndex += 1
            else:
                stackTopIndex = stack[-1]
                stack.pop()
                maxRectangleArea = max(maxRectangleArea, heights[stackTopIndex]*(searchIndex if not stack else searchIndex - stack[-1] -1))
        return maxRectangleArea

solve = Solution()
print(solve.largestRectangleArea([1]))


