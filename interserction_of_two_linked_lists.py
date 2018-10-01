# Definition for singly-linked list.
class ListNode(object):
    def __init__(self, x):
        self.val = x
        self.next = None


class Solution(object):
    def getIntersectionNode(self, headA, headB):
        """
        :type head1, head1: ListNode
        :rtype: ListNode
        """

        point_a = headA
        point_b = headB
        while point_a != point_b:
            point_a = headB if not point_a else point_a.next
            point_b = headA if not point_b else point_b.next
        return point_a

if __name__ == '__main__':
    node1 = ListNode(1)
    node2 = ListNode(2)
    node3 = ListNode(3)
    node4 = ListNode(4)
    node5 = ListNode(5)
    node7 = ListNode(7)
    node9 = ListNode(9)
    node11 = ListNode(11)
    node1.next = node3
    node3.next = node5
    node5.next = node7
    node7.next = node9
    node9.next = node11
    node2.next = node4
    node4.next = node9

    print(Solution().getIntersectionNode(node1, node2).val)
