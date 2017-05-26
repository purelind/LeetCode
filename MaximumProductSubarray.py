"""
152. Maximum Product Subarray
Find the contiguous subarray within an array (containing at least one
number) which has the largest product.
For example, given the array [2, 3, -2, 4],
the contiguous subarray [2, 3] has the largest product = 6
"""
# def maxProduct(nums):
#     """
#
#     :param nums: List[int]
#     :return: int
#     """
#     i = 0
#     if len(nums) == 1:
#         return nums[0]
#     else:
#         maxValue = nums[i] * nums[i+1]
#         i += 1
#         while i < len(nums)-1:
#             test_Value = nums[i] * nums[i+1]
#             if test_Value > maxValue:
#                 maxValue = test_Value
#             i += 1
#         return maxValue
#
# print(maxProduct([2, 3, 2, 2]))


def maxProduct(nums):
    """

    :param nums: List[int]
    :return: int
    """
    def find_contiguous_positive_subarray(array):
        """
        
        :param array: List[int] 
        :return: List[list]
        """

