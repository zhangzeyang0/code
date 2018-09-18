# Definition for singly-linked list.
class ListNode(object):
    def __init__(self, x):
        self.val = x
        self.next = None

class Solution(object):
    def reverseKGroup(self, head, k):
        """
        :type head: ListNode
        :type k: int
        :rtype: ListNode
        """
        res = ListNode(0)
        res.next = head
        for i in range(k):
            res = res.next
            if not res:
                return head

        pre_node = ListNode(0)
        stack = []
        node = head
        while node:
            for i in range(k):
                if node is None:
                    return res
                stack.append(node)
                node = node.next
            next_node = node
            pre_node.next = stack[-1]
            for j in range(k-1):
                tmp = stack.pop()
                tmp.next = stack[-1]
            tmp = stack.pop()
            tmp.next = next_node
            pre_node = tmp
            node = next_node
        return res
t = Solution()
a1 = ListNode(1)
a2 = ListNode(2)
a3 = ListNode(3)
a4 = ListNode(4)
a5 = ListNode(5)
a1.next = a2
a2.next = a3
a3.next = a4
a4.next = a5
node = t.reverseKGroup(a1, 2)
# print(node.next.val)
while node:
    print(node.val)
    node = node.next


