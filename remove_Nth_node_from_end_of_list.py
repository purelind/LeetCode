# Definition for singly-linked list.
class ListNode(object):
    def __init__(self, x):
        self.val = x
        self.next = None


class Solution(object):
    def removeNthFromEnd(self, head, n):
        """
        :type head: ListNode
        :type n: int
        :rtype: ListNode
        """
        fast = slow =head
        for i in range(n):
            fast = fast.next
        if not fast:
            return head.next
        while fast.next:
            fast = fast.next
            slow = slow.next
        slow.next = slow.next.next
        return head

# 两个指针进行索引，fast索引超前slow索引n个位置
# 当fast索引指向链表最后一个元素的时候，slow指向倒数第n+1个元素
# 此时依照题意，删除倒数第n个元素，将slow.next指向slow.next.next
# 这个时候，之前slow.next指向的元素就会没有指针指向它了,删除倒数第n个元素的目的就达到了
# 难点，关于倒数第n个元素恰好是首个元素的情况：
# 这种情况下，fast指针向后移动n个位置后，指向的一定是最后的元素的后一个元素，就是空None
# 此时，我们返回第二个元素即可（head.next）

