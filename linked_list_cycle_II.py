# Definition for singly-linked list.
# class ListNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.next = None

class Solution(object):
    def detectCycle(self, head):
        """
        :type head: ListNode
        :rtype: ListNode
        """
        if not head or not head.next:
            return None

        firstp = head
        secondp = head
        is_cycle = False

        while  firstp and  secondp:
            firstp = firstp.next
            if not secondp.next:
                return None
            secondp = secondp.next.next
            if firstp == secondp:
                is_cycle = True
                break

        if not is_cycle:
            return None
        firstp = head
        while firstp != secondp:
            firstp = firstp.next
            secondp = secondp.next

        return firstp


