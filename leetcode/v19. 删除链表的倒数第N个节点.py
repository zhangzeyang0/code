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
        length = self.get_length(head)
        cnt = length-n-1
        if cnt < 0:
            return head.next
        res = ListNode(0)
        res.next = head
        node = head
        for i in range(cnt):
            node = node.next
        node.next = node.next.next
        return head


    def get_length(self, node):
        cnt = 0
        while node:
            cnt += 1
            node = node.next
        return cnt
a1 = ListNode(1)
a2 = ListNode(2)
a3 = ListNode(3)
a4 = ListNode(4)
a5 = ListNode(5)
a1.next = a2
a2.next = a3
a3.next = a4
a4.next = a5
t = Solution()
node = t.removeNthFromEnd(a1)
