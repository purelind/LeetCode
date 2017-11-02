# Definition for singly-linked list.
class ListNode(object):
    def __init__(self, x):
        self.val = x
        self.next = None


class Solution(object):
    # iteratively迭代
    def mergeTwoLists(self, l1, l2):
        """
        :type l1: ListNode
        :type l2: ListNode
        :rtype: ListNode
        dummy 哑节点，常常作为辅助节点
        cur (current) 指向当前比较的节点
        """
        # 使用一个辅助Node节点，初始的时候dummy和cur都指向节点ListNode(0)
        # cur指针会一直走下去，dummy用来最后指向新的链表的第一个节点
        dummy = cur = ListNode(0)

        # while循环，当l1 与l2 两个链表都还存在 Node,一直循环下去
        while l1 and l2:
            # 比较l1和l2目前指向的Node节点的value
            if l1.val < l2.val:
                cur.next = l1  # cur指针指向较小的值，新链表的一个节点确定
                l1 = l1.next  # l1继续向下走
            else:
                cur.next = l2
                l2 = l2.next
            cur = cur.next  # cur指针向下走
        # 当l1或l2链表的Node节点取尽的时候，跳出while循环
        # 如果l1节点取尽，cur.next = l2, cur指向l2剩余的节点的第一个节点
        # 如果l1节点未取尽，l2节点取尽，cur.next = l1, cur指向l1剩余的节点的第一个节点
        cur.next = l1 or l2

        # dummy用于寻找新链表的第一个节点，新链表的指针cur从ListNode(0)出发，从而形成新链表
        # 而dummy也是指向节点ListNode(0)
        return dummy.next

    # recursively递归
    def mergeTwoLists2(self, l1, l2):
        # l1或l2未空，返回非空的链表，无需比较
        if not l1 or not l2:
            return l1 or l2
        # 方法mergeTwoList2(),传入两个链表参数，返回一个排好序的新链表
        #　mergeTwoLists(l1.next, l2)必定将返回一个排好序的新链表，之后
        #　　将l1链表第一个节点指向返回的新链表，那么将得到一个完整的链表
        # 递归的思想就是形成多层次的嵌套，然后从递归的最底层向上返回
        if l1.val < l2.val:
            l1.next = self.mergeTwoLists(l1.next, l2)
            return l1
        else:
            l2.next = self.mergeTwoLists(l1, l2.next)
            return l2

