class Solution(object):
    def isValid(self, s):
        """
        :type s: str
        :rtype: bool
        """
        stack = []
        dict = {"]": "[", "}": "{", ")": "("}
        for char in s:
            if char in dict.values():
                stack.append(char)
            elif char in dict.keys():
                if not stack or dict[char] != stack.pop():
                    return False
            else:
                return False
        return stack == []

solve = Solution()
print(solve.isValid('([])'))


# 将括号左半部作为key,右半部作为value
# 将所有出现的左半部括号压入栈
# 遇见右半部括号，如果stack为空，此时没有一个左半部括号与其对应，必定return False
# stack非空，弹出栈顶的元素，如果和该右半部括号不配对，return False
# 最后，如果栈stack中没有元素剩余，则全部配对。如果，s为''，也认为全部配对
