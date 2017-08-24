class Solution(object):
    def convert(self, s, numRows):
        """
        :type s: str
        :type numRows: int
        :rtype: str
        """
        step = (numRows == 1) - 1
        rows, idx = [''] * numRows, 0
        for c in s:
            rows[idx] += c
            if idx == 0 or idx == numRows-1:
                step = -step
            idx += step
        return ''.join(rows)

sovle = Solution()
print(sovle.convert('PAYPALISHIRING', 3))