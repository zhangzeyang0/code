# Definition for singly-linked list.
class ListNode(object):
    def __init__(self, x):
        self.val = x
        self.next = None

class Solution(object):
    '''
    交换结点，注意要保存3个结点，当前要交换的2个结点和这个2个结点之前的结点
    '''
    def swapPairs(self, head):
        if not head:
            return None
        res = p1 = ListNode(0)
        res.next = head
        while p1.next and p1.next.next:
            p0, p1, p2 = p1, p1.next, p1.next.next
            p0.next, p1.next, p2.next = p2, p2.next, p1
        print(p1.next.val, res.next.val)
        return res.next


    def swapPairs2(self, head):
        """
        :type head: ListNode
        :rtype: ListNode
        """
        if not head or head.next is None:
            return head
        pre = head
        nxt = head.next.next
        head = head.next
        head.next = pre
        pre.next = nxt

        pre_node = head.next

        node = head.next.next
        while node and node.next:
            pre = node
            nxt = node.next.next
            node = node.next
            node.next = pre
            pre.next = nxt
            pre_node.next = node

            pre_node = node.next
            node = pre_node.next
        return head
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
node = t.swapPairs(a1)
while node:
    print(node.val)
    node = node.next


