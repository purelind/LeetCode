class Solution(object):
    def letterCombinations(self, digits):
        """
        :type digits: str
        :rtype: List[str]
        """
        if not digits:
            return []
        kvmaps = {
            '2': 'abc',
            '3': 'def',
            '4': 'ghi',
            '5': 'jkl',
            '6': 'mno',
            '7': 'pqrs',
            '8': 'tuv',
            '9': 'wxyz'
        }
        from functools import reduce
        return reduce(lambda acc, digits: [x + y for x in acc for y in kvmaps[digits]], digits, [''])


#  functools.reduce(function, iterable[, initializer])
# @ funtion ==> lambda函数
# @ iterable ==> digits字符串
# @ initializer ==> 初始化参数为空字符''
# 难点：　reduce的使用，从左至右，将函数累积的应用在一系列元素上面，最终将这列元素转化为一个元素
# lambda参数：　首先参数digits好理解，参数digits从上层函数作用域中变量名digits中获取。
# 难点在于lambda中的acc参数，当reduce函数初次调用lambda的函数的时候，参数acc从所有作用域中的获取
# 不到。所以此时为空；而reduce第二次调用lambda函数的时候，：function(function(kvmap(0)), kvmap(1));
# 可以将acc看作是保存暂时结果的的list，该list会保存对于当前digits中的digit得到的[x + y for x in acc for y in kvmaps[digits]]
# 结果。即acc等同于function(kvmap(current_digit))

# 不知道解释对不对。暂且这样理解.
# 链接：https://discuss.leetcode.com/topic/11783/one-line-python-solution/16


solve = Solution()
print(solve.letterCombinations('23'))