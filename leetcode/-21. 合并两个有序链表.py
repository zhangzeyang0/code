# Definition for singly-linked list.
class ListNode(object):
    def __init__(self, x):
        self.val = x
        self.next = None

class Solution(object):
    def mergeTwoLists1(self, l1, l2):
        """
        :type l1: ListNode
        :type l2: ListNode
        :rtype: ListNode
        """
        if not l1:
            return l2
        elif not l2:
            return l1
        res = ListNode(0)
        self.merge_core(l1, l2, res)
        return res.next
    def merge_core(self, l1, l2, head):
        temp1 = 1
        temp2 = 1
        while l1 and l2:
            if l1.val <= l2.val:
                head.next = l1
                while l1.next and l1.next.val <= l2.val:
                    l1 = l1.next
                temp1 = l1.next
                l1.next = l2
                l2 = l2.next
                l1.next.next = temp1
                head = l1.next
                if temp1 is None:
                    l1 = l1.next
                    break
                else:
                    l1 = temp1
            elif l1.val > l2.val:
                head.next = l2
                while l2.next and l2.next.val <= l1.val:
                    l2 = l2.next
                temp2 = l2.next
                l2.next = l1
                l1 = l1.next
                l2.next.next = temp2
                head = l2.next
                if temp2 is None:
                    l2 = l2.next
                    break
                else:
                    l2 = temp2
        if not temp1:
            head.next = l2
        elif not temp2:
            head.next = l1


    def mergeTwoLists(self, l1, l2):
        """
        :type l1: ListNode
        :type l2: ListNode
        :rtype: ListNode
        """
        head = ListNode(None)
        cur = head
        head.next = l1
        while l1 and l2:
            if l1.val <= l2.val:
                l1 = l1.next
            else:
                temp = cur.next
                cur.next = l2
                l2 = l2.next
                cur.next.next = temp
            cur = cur.next
        cur.next = l1 or l2
        return head.next
t = Solution()
a0 = ListNode(2)
a1 = ListNode(1)
# a2 = ListNode(5)
# a3 = ListNode(7)
# a0.next = a1
# a2.next = a3
head = t.mergeTwoLists(a0, a1)
while head:
    print(head.val)
    head = head.next
