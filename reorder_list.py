# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, x):
#         self.val = x
#         self.next = None


class Solution:
    def reorderList(self, head):
        """
        :type head: ListNode
        :rtype: void Do not return anything, modify head in-place instead.
        """
        if not head or not head.next:
            return

        #: Find the middle of the list
        p1 = head
        p2 = head
        while p2.next and p2.next.next:
            p1 = p1.next
            p2 = p2.next.next

        #: Reverser the half after middle 1->2->3->4->5->6 to 1->2->3->6->5->4
        pre_middle = p1
        pre_current = p1.next
        while pre_current.next:
            current = pre_current.next
            pre_current.next = current.next
            current.next = pre_middle.next
            pre_middle.next = current

        #: Start reorder one by one 1->2->3->6->5->4 to 1->6->2->5->3->4
        p1 = head
        p2 = pre_middle.next
        while p1 != pre_middle:
            pre_middle.next = p2.next
            p2.next = p1.next
            p1.next = p2
            p1 = p2.next
            p2 = pre_middle.next
